import sys, dewiki, json, requests

def from_wiki(elem):
    params = {
        'action': 'parse',
        'page': elem,
        'format': 'json',
        'prop': 'wikitext',
        'redirects': 1
    }
    resp = requests.get('https://en.wikipedia.org/w/api.php', params=params)
    resp.raise_for_status()
    resp = json.loads(resp.text)
    if 'error' in resp:
        raise Exception('Page error')
    return dewiki.from_string(resp['parse']['wikitext']['*'])

def request_wikipedia():
    args = sys.argv
    if len(args) != 2:
        return print('Wrong number of arguments')
    try:
        my_file = open(f'{args[1]}.wiki', 'w')
        my_file.write(from_wiki(args[1]))
    except Exception as exc:
        print(exc)

if __name__ == '__main__':
    request_wikipedia()