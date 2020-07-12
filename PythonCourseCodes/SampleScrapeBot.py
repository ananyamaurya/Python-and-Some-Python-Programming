import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')


def create_custom_fn(links, votes):
    hack_news = {}
    for inx, item in enumerate(links):
        title = links[inx].get_text()
        href = links[inx].get('href', None)
        points = votes[inx].get_text()
        a, b = points.split()

        if int(a) > 100:
            hack_news.update({title: href})

    return hack_news


for k, h in create_custom_fn(links, votes).items():
    print(str(k) + '\n' + str(h) + '\n\n')
