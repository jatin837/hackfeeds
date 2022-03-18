from scrape import fetch
from jinja2 import Template


data = fetch()

class feed():
    def __init__(self, headline, link):
        self.headline = headline
        self.link = link
    def __repr__(self):
        return f"{self.headline} -- {self.link}"

feeds = [feed(data['headline'][i], data['link'][i]) for i in range(len(data['headline']))]

with open('mail.html', 'r') as f:
    content = f.read()

tm = Template(content)
msg = tm.render(feeds=feeds)
print(msg)

with open('out.html', 'w') as f:
    f.write(msg)
