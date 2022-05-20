class Intern(object):
    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        self.name = name
    
    def _str__(self):
        return self.name
    
    class Coffee():
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()

def my_intern():
    intern_1 = Intern()
    intern_2 = Intern("Mark")
    print("|---------Intern 1---------|")
    print(f"{intern_1.name}")
    print(f"{intern_1.make_coffee()}")
    try:
        intern_1.work()
    except Exception as exc:
        print(f"{exc}")
        
    print("|---------Intern 2---------|")
    print(f"{intern_2.name}.")
    print(f"{intern_2.make_coffee()}")
    try:
        intern_2.work()
    except Exception as exc:
        print(f"{exc}")

if __name__ == '__main__':
    my_intern()