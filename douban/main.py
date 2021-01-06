from scrapy import cmdline
cmdline.execute('scrapy crawl douban_spider -o ../../output.json'.split())
