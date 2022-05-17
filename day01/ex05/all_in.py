import sys

def search_value(my_dict, elem):
    for key, value in my_dict.items():
        if value.lower() == elem.lower():
            return value
    return None

def search_key(my_dict, elem):
    for key, value in my_dict.items():
        if key.lower() == elem.lower():
            return key
    return None

def search(my_dict, val):
    for key, value in my_dict.items():
        if value == val:
            return key
    return None

def my_search(elem):
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
    my_dict = dict(zip(capital_cities.values(), states.keys()))
    key = search_key(my_dict, elem)
    if key:
        print(f'{key} is the capital of {my_dict[key]}')
    if key == None:
        value = search_value(my_dict, elem)
        if value != None:
            key = search(my_dict, value)
            print(f'{key} is the capital of {my_dict[key]}')
        else:
            print(f'{elem} is neither a capital city nor a state')

def state():
    if len(sys.argv) != 2:
        return 
    state = [elem.strip() for elem in sys.argv[1:][0].split(',') if elem.strip() != '']
    for elem in state:
        my_search(elem)
    
if __name__ == '__main__':
    state()