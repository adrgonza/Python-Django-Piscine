import requests
import json
import dewiki
import sys

def main():
    if len(sys.argv) != 2:
        print("You must send an argument")
        return
    
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "format": "json",
        "prop": "wikitext",
        "page": sys.argv[1]
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if data.get("error") is not None:
            print("Page not found")
            return
        extract = dewiki.from_string(data["parse"]["wikitext"]["*"])
    except requests.RequestException as e:
        print(f"Error making request to Wikipedia API: {e}")
        return

    try:
        with open(sys.argv[1].replace(' ', '_') + ".wiki", "w") as file:
            file.write(extract)
    except Exception as e:
            print(f"An error occurred: {e}")
    
if __name__ == "__main__":
    main()