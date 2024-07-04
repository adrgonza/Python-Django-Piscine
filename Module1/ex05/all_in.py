import sys

def search_key_with_value(my_dict, value):
    for key, val in my_dict.items():
        if val == value:
            return key
    return None

def parse_arg(arg):
    return arg.strip().title() if arg else ""

def manage_dictionaries(states, capital_cities):
    argc = len(sys.argv)
    if argc != 2:
        return
        
    args = sys.argv[1].split(",")
    for arg in args:
        arg = parse_arg(arg)
        if not arg:
            continue
        try:
            key_states = states[arg]
            state_value = arg
            capital_value = capital_cities[key_states]
        except:
            key_capital = search_key_with_value(capital_cities, arg)
            if key_capital:
                state_value = search_key_with_value(states, key_capital)
                capital_value = arg
            else:
                print(arg + " is neither a capital city or a state")
                continue
        print(capital_value + "  is the capital of " + state_value)

if __name__ == '__main__':
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
    manage_dictionaries(states, capital_cities)
