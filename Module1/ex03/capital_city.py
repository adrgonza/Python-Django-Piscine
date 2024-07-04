import sys

n = len(sys.argv)
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

def search_dict():
    if n != 2:
        return 0
    try:
        key = states[sys.argv[1]]
        print(capital_cities[key])
    except:
        print("Unknown state")

if __name__ == "__main__":
    search_dict()
