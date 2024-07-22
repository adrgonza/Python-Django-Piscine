import requests
import json
import dewiki
import sys

def main():
    if len(sys.argv) != 2:
        return
    
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": True,
        "titles": sys.argv[1]
    }
    try:
        response = requests.get(url, params=params)
    except requests.RequestException as e:
        print(f"Error making request to Wikipedia API: {e}")
        return
    data = response.json()
    pages = data.get("query", {}).get("pages", {})
    page = next(iter(pages.values()), {})
    extract = page.get("extract", "")

    if not extract:
        print(f"No extract found for page: {sys.argv[1]}")
        return

    extract = dewiki.from_string(extract)
    print(extract)

    #with open(sys.argv[1] + ".wiki", "w") as file:
        #file.write(response)
    

if __name__ == "__main__":
    main()