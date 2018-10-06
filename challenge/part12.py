# webページのスクレイピング

import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "http" in url:
                if tag.string is not None:
                    print("\n" + tag.string)
                    print("\n" + url)
                    print(" --- \n")
    
# news = 'https://news.google.com/'
news = 'http://b.hatena.ne.jp/hotentry/it'
Scraper(news).scrape()