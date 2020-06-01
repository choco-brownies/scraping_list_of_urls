ScrapingListOfURLS tool is used to scrape all web pages with urls provided in file: `source_links.txt`.

In `scrapeurls/scrapeurls/spiders/scrape_urls_spider.py` define proper css selectors related to the website you want to
scrape.

The tool can be ran successfully if the following instructions are followed:

* Clone the repository:
```
git clone https://github.com/choco-brownies/scraping_list_of_urls.git
```
* In the scraping_list_of_urls directory create and activate virtual environment:
```
cd scraping_list_of_urls
virtualenv -p python3 venv
source venv/bin/activate
```
* Install all dependencies from the file requirements.txt:
```
pip install -r requirements.txt
```

* Start Web Scraper tool:
```
scrapy crawl urls
```