import sys

def search_key_with_value(my_dict, value):
    for key, val in my_dict.items():
        if val == value:
            return key
    return None

def capital_to_state(states, capital_cities):
    if len(sys.argv) != 2:
        return 0
    key = search_key_with_value(capital_cities, sys.argv[1])
    if key:
        print(search_key_with_value(states, key))
        return 0
    print("Unknown capital city")
    
if __name__ == "__main__":
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
    capital_to_state(states, capital_cities)