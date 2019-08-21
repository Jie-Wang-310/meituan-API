from scrapy import cmdline
cmdline.execute("scrapy crawl food -o test.json -t json".split())