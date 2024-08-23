import sys
import requests
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) != 2:
        return print("You must provide exactly 1 argument.")
    
    titles = []
    url = "https://en.wikipedia.org/wiki/"
    page = sys.argv[1].replace(' ', '_')
    
    while True:
        content = requests.get(url + page).text
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.title.string.replace(" - Wikipedia", "")
        
        if title in titles:
            return print("This is an infinite loop!")
        
        titles.append(title)

        if title.lower() == "philosophy":
            print(*titles, sep="\n")
            return print(f"{len(titles)} steps from {sys.argv[1]} to Philosophy!")
        
        text = soup.find(id='mw-content-text')
        all_links = text.select('p > a')

        if not all_links:
            if len(titles) == 1:
                return print("The page does not exist!")
            return print("It leads to a dead end!")
        for link in all_links:
            link_text = link.find_parent('p').text
            link_text_before = link_text.split(link.text)[0]
            if link.get('href') and link_text_before.count('(') == link_text_before.count(')'):
                page = link['href'][6:]
                break
        
        if not page:
            return print("No valid links found. It leads to a dead end.")

if __name__ == "__main__":
    main()
