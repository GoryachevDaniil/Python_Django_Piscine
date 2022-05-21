import sys, requests
from bs4 import BeautifulSoup

def result(title, my_list, soup):
    print(title)
    if title == 'Philosophy':
        return print(f"{len(my_list)} roads from {my_list[0]} to philosophy !")
    content = soup.find(id='mw-content-text')
    links = content.select('p > a')
    for link in links:
        if link.get('href') is not None and link['href'].startswith('/wiki/') \
                            and not link['href'].startswith('/wiki/Wikipedia:')\
                            and not link['href'].startswith('/wiki/Help:'):
            return wiki(link['href'], my_list)
    return print("It's a dead end !")

def wiki(title, my_list):
    resp = requests.get(url=f'https://en.wikipedia.org{title}')
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    title = soup.find(id='firstHeading').text
    if title in my_list:
        return print("Произошло зацикливание")
    my_list.append(title)
    result(title, my_list, soup)

def roads_to_philosophy():
    args = sys.argv
    if len(args) != 2:
        return print('Введите один аргумент')
    try:
        my_list = []
        wiki(f'/wiki/{args[1]}', my_list)
    except Exception as exc:
        print(exc)

if __name__ == '__main__':
    roads_to_philosophy()