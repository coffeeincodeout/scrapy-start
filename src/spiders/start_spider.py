import scrapy
from scrapy.crawler import CrawlerProcess

import os
import sys


class StartSpider(scrapy.Spider):
    """
    Starter scraper for scrapy so you dont have
    to keep setting up the same settings.
    """
    name = 'start'
    base_url = 'url'
    start_url = [
        'place urls here '
    ]
    # change the file name of you plan to use flat storage
    TMP_FILE = os.path.join(os.path.dirname(sys.modules['forklift'].__file__), 'tmp/filename.csv')
    # enter the field names below to format the output in your csv file
    FIELDS = [
        'name',
        'address',
        'your-info',
    ]
    # custom setting per spider if not needed then remove and adjust crawl in settings
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': TMP_FILE,
        'FEED_EXPORT_FIELDS': FIELDS,
        'DOWNLOAD_DELAY': 8,
        'CONCURRENT_REQUESTS': 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 8,
    }

    def parse(self, response):
        pass


# concurrent process to run all forklifts at the same time.
process = CrawlerProcess()
process.crawl(StartSpider)
process.start()
