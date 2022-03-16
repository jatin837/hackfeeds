import requests as r
from bs4 import BeautifulSoup

def fetch():
    url = 'https://news.ycombinator.com/'

    res = r.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')

    data = {
        'headline': [],
        'link': [],
    }

    for athing in soup.findAll(class_ = 'athing'):
        content = athing.findAll('td')[2]
        data['headline'].append(content.a.get_text())
        data['link'].append(content.a['href'])

    return data

def send(msg = '', to = []):
    # send text message to email list
    pass
