import requests as r
from bs4 import BeautifulSoup


url = 'https://news.ycombinator.com/'

res = r.get(url)


soup = BeautifulSoup(res.content, 'html.parser')

for athing in soup.findAll(class_ = 'athing'):
    data = athing.findAll('td')[2]
    print(data.a.get_text(), data.a['href'])
