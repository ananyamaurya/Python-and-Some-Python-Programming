
import requests
import csv
from bs4 import BeautifulSoup

hack_news = []


def get_soup(n):
    for i in range(n):
        res = requests.get(f'https://news.ycombinator.com/news?p={i+1}')
        soup = BeautifulSoup(res.text, 'html.parser')
        link_news = soup.select('.storylink')
        subtext_news = soup.select('.subtext')
        create_custom_fn(link_news, subtext_news)

    return sorted_news(hack_news)


class News:
    title = ""
    href = ""
    vote = 0

    def __init__(self, title, href, vote):
        self.title = title
        self.href = href
        self.vote = vote


def sorted_news(hack_n):
    return sorted(hack_n, key=lambda x: x.vote, reverse=True)


def create_custom_fn(link_new, subtext_new):

    for inx, item in enumerate(link_new):
        title = link_new[inx].get_text()
        href = link_new[inx].get('href', None)
        vote = subtext_new[inx].select('.score')
        if len(vote):
            points = int(vote[0].get_text().replace(" points", ''))
            if points >= 100:
                x = News(title, href, points)
                hack_news.append(x)

    return


filename = "hackernew-records.csv"
fields = ['Votes', 'News Title', 'News Link']
# writing to csv file
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile,  delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(fields)
    for i in get_soup(4):
        l = [i.vote,i.title, i.href]
        csvwriter.writerow(l) 
        print(f"{i.title} \n{i.vote} votes : Link {i.href}\n\n")
