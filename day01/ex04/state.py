import sys

def state():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    if len(sys.argv) != 2:
        return 
    state = sys.argv
    my_dict = dict(zip(capital_cities.values(), states.keys()))
    if state[1] in my_dict:
        print(my_dict[state[1]])
    else:
        print("Unknown capital city")

if __name__ == '__main__':
    state()