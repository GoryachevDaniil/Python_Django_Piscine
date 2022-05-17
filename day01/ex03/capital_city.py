import sys

def capital_city():
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

    if state[1] in states.keys():
        print(capital_cities.get(states[state[1]]))
    else:
        print("Unknown state")


if __name__ == '__main__':
    capital_city()