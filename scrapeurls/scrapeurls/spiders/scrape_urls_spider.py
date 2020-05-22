import scrapy
from ..items import ScrapeurlsItem
from datetime import datetime
from ..Selector import Selector

class ScrapeUrlsSpider(scrapy.Spider):
    name = 'urls'
    with open("source_links.txt", "rt") as f:
        lines = [url.strip().split(" : ") for url in f]

    lines = [line for line in lines if line[1].startswith("http://www.nytimes.com") or line[1].startswith("https://www.nytimes.com") or line[1].startswith("http://online.wsj.com")]
             # or line[1].startswith("http://www.washingtonpost.com") or line[1].startswith("https://www.washingtonpost.com")]
    start_urls = [line[1] for line in lines]

    def parse(self, response):
        items = ScrapeurlsItem()
        if response.request.meta.get('redirect_urls'):
            url = response.request.meta.get('redirect_urls')[0]
        else:
            url = response.request.url
        ind = self.start_urls.index(url)
        date_of_scraping = datetime.today().strftime('%d%m%Y')
        if response.request.url.startswith("http://www.nytimes.com") or response.request.url.startswith("https://www.nytimes.com"):
            selector = Selector(title='h1.e1h9rw200::text', date_of_publishing='.e16638kd0::text, .e16638kd4::text', text='.evys1bk0::text')
        elif response.request.url.startswith("http://online.wsj.com") or response.request.url.startswith("https://online.wsj.com"):
            selector = Selector(title='.sub-head::text, .wsj-article-headline::text', date_of_publishing='.timestamp::text', text='#wsj-article-wrap p::text')
        elif response.request.url.startswith("http://www.washingtonpost.com") or response.request.url.startswith("https://www.washingtonpost.com"):
            selector = Selector(title='h1::text', date_of_publishing='.author-timestamp::text, .display-date::text',
                                text='p::text')
        else:
            return

        items['id'] = self.lines[ind][0]
        items['title'] = response.css(selector.title).extract()
        items['date_of_publishing'] = response.css(selector.date_of_publishing).extract()
        items['link'] = response.request.url
        items['date_of_scraping'] = date_of_scraping
        items['text'] = response.css(selector.text).extract()
        yield items

