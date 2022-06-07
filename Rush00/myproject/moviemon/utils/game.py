import random
import requests
import os
from django.conf import settings
import pickle
import glob


class GameObject:
    def __init__(self, x=0, y=0):
        self.pos_x = x
        self.pos_y = y

    def x_position(self):
        return self.pos_x

    def y_position(self):
        return self.pos_y

    def position(self):
        return self.pos_x, self.pos_y


class Player(GameObject):

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.power = 0

    def load_default_settings(self):
        self.pos_x = settings.START_POINT[0]
        self.pos_y = settings.START_POINT[1]

    def load_data(self, cache):
        if cache is None:
            raise Player.PlayerClassError("no cache file")
        self.pos_x = cache['player_pos'][0]
        self.pos_y = cache['player_pos'][1]
        self.power = cache['strength']

    def strength(self):
        return self.power

    def move(self, x_inc, y_inc):
        dest_pos_x = self.pos_x + x_inc
        dest_pos_y = self.pos_y + y_inc
        return dest_pos_x, dest_pos_y

    def percentage(self, monster_power):
        atk = 50 - int(monster_power * 10) + (self.strength() * 5)
        if atk < 1:
            atk = 1
        if atk > 90:
            atk = 90
        return atk

    def attack(self, monster_power):
        atk = self.percentage(monster_power)
        r_num = random.randrange(0, 100)
        if r_num < atk:
            return True
        return False

    @staticmethod
    class PlayerClassError(Exception):
        def __init__(self, msg='Error'):
            super().__init__(msg)


class World:

    def __init__(self, size_x=settings.GRID_SIZE, size_y=settings.GRID_SIZE):
        self.grid_x = size_x
        self.grid_y = size_y

    def load_default_settings(self):
        self.grid_x = settings.GRID_SIZE
        self.grid_y = settings.GRID_SIZE

    def load_data(self, cache):
        pass


class Movie:

    def __init__(self):
        self.captured = []

    def load_default_settings(self, lst=settings.MOVIES):
        try:
            dic = {}
            for movie in lst:
                this_json = Movie.get_movie(movie)
                dic[movie] = this_json
            self.moviedex = dic
        except Movie.MovieClassError as e:
            print(e)

    def load_data(self, cache):
        if cache is None:
            raise Movie.MovieClassError("no cache file")
        self.captured = cache['captured']
        self.moviedex = cache['moviedex']

    def __check_captured_dup(self, add):
        dup = self.captured
        dup.append(add)
        if len(dup) == len(set(dup)):
            dup.remove(add)
            return True
        dup.remove(add)
        return False

    def capture(self, idx):
        if self.__check_captured_dup(idx) == True:
            self.captured.append(idx)

    def get_random_movie(self):
        result = False
        while result == False:
            idx = random.choice(settings.MOVIES)
            result = self.__check_captured_dup(idx)
        return idx, self.moviedex[idx]

    @staticmethod
    def get_movie(idx=''):
        params = {'i': idx, 'r': 'json', 'apikey': "b02fca2"}
        url = 'http://www.omdbapi.com/'
        response = requests.get(url, params=params)
        if response.ok == False:
            raise Movie.MovieClassError("request error")
        my_json = response.json()
        return my_json

    @staticmethod
    class MovieClassError(Exception):
        def __init__(self, msg='Error in MovieClassError'):
            super().__init__(msg)


class Game:

    def __init__(self):
        self.player = Player()
        self.world = World()
        self.movie = Movie()
        self.movie_balls = 0
        self.battle = False
        self.battle_result = None

    def load_default_settings(self):
        self.player.load_default_settings()
        self.world.load_default_settings()
        self.movie.load_default_settings()
        self.movie_balls = settings.BALL_COUNT

    def dump_data(self):
        return {
            'player_pos': self.player.position(),
            'ball_count': self.movie_balls,
            'strength': self.player.strength(),
            'captured': self.movie.captured,
            'moviedex': self.movie.moviedex,
            'battle': self.battle,
        }

    def load_data(self, cache):
        try:
            if cache == None:
                raise Game.GameClassError("no cache file")
            self.player.load_data(cache)
            self.world.load_data(cache)
            self.movie.load_data(cache)
            self.movie_balls = cache['ball_count']
            self.battle = cache['battle']
        except Game.GameClassError as e:
            print(e)

    def get_strength(self):
        return self.player.strength()

    def get_random_movie(self):
        return self.movie.get_random_movie()

    @staticmethod
    def get_movie(idx=''):
        return Movie.get_movie(idx)

    def __move_player_Up(self):
        if self.player.y_position() >= self.world.grid_y - 1:
            return None
        return self.player.move(0, 1)

    def __move_player_Down(self):
        if self.player.y_position() <= 0:
            return None
        return self.player.move(0, -1)

    def __move_player_Right(self):
        if self.player.x_position() >= self.world.grid_x - 1:
            return None
        return self.player.move(1, 0)

    def __move_player_Left(self):
        if self.player.x_position() <= 0:
            return None
        return self.player.move(-1, 0)

    _player_move = {
        'Up': __move_player_Down,
        'Down': __move_player_Up,
        'Left': __move_player_Left,
        'Right': __move_player_Right
    }

    def move_player(self, order):
        return (self._player_move[order](self))

    def battle_start(self):
        self.battle = True

    def battle_end(self):
        self.battle_result = None
        self.battle = False

    def battle_status(self):
        return self.battle

    def player_Attack(self, m_id=None):
        if self.movie_balls <= 0:
            return None
        self.movie_balls -= 1
        if self.player.attack(float(self.movie.moviedex[m_id]['imdbRating'])) == True:
            self.movie.capture(m_id)
            self.player.power = len(self.movie.captured)
            return True
        else:
            return False

    def dump_cache(self, _cache):
        try:
            with open('cache.pkl', 'wb') as cache:
                pickle.dump(_cache, cache)
        except Game.GameClassError as e:
            print(e)

    def load_cache(self):
        try:
            self.cache = {}
            with open('cache.pkl', 'rb') as cache:
                self.cache = pickle.load(cache)
            return self.cache
        except Game.GameClassError as e:
            print(e)

    @staticmethod
    class GameClassError(Exception):
        def __init__(self, msg='Error in GameClassError'):
            super().__init__(msg)


class GameData:

    @staticmethod
    def str_builder(idx='', movie_balls=settings.BALL_COUNT, score=0):
        return "saved_game/slot{idx}_{ball}_{score}.mmg".format(idx=idx,
                                                                ball=movie_balls,
                                                                score=score)

    @staticmethod
    def save(idx=''):
        try:
            if not os.path.exists('saved_game'):
                os.makedirs('saved_game')
            with open('cache.pkl', 'rb') as _cache:
                cache = pickle.load(_cache)
            for p in glob.glob('saved_game/slot' + idx + '_*_*.mmg'):
                os.remove(p)
            if len(cache) > 0:
                with open(GameData.str_builder(idx, len(cache['captured']),
                                               len(cache['moviedex'])), 'wb') as file:
                    pickle.dump(cache, file)
                    return True
            return False
        except GameData.GameDataError as e:
            print(e)
            return False

    @staticmethod
    def load(idx=''):
        try:
            if not os.path.exists('saved_game'):
                return False
            file_name = glob.glob('saved_game/slot' + idx + '_*_*.mmg')
            if len(file_name) > 1 or len(file_name) == 0:
                return False
            with open(file_name[0], 'rb') as file:
                data = pickle.load(file)
            with open('cache.pkl', 'wb') as cache:
                pickle.dump(data, cache)
            return True
        except GameData.GameDataError as e:
            print(e)
            return False

    @staticmethod
    def __make_slot_name(slot_file_name=''):
        name_list = slot_file_name.replace('saved_game/', '').split('_')
        name = name_list[1] + '/' + name_list[2].replace('.mmg', '')
        return name

    @staticmethod
    def get_save_list():
        sav_lst = ['Free', 'Free', 'Free']
        a_file = glob.glob('saved_game/slotA_*_*.mmg')
        if len(a_file) == 1:
            sav_lst[0] = GameData.__make_slot_name(a_file[0])
        b_file = glob.glob('saved_game/slotB_*_*.mmg')
        if len(b_file) == 1:
            sav_lst[1] = GameData.__make_slot_name(b_file[0])
        c_file = glob.glob('saved_game/slotC_*_*.mmg')
        if len(c_file) == 1:
            sav_lst[2] = GameData.__make_slot_name(c_file[0])
        return sav_lst

    @staticmethod
    class GameDataError(Exception):
        def __init__(self, msg='GameDataError : game.py'):
            super().__init__(msg)

