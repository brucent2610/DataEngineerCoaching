# from scrapy import cmdline    
# cmdline.execute("scrapy crawl GpusVideoGraphicsCards".split())

import urllib.request
source = urllib.request.urlopen('https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48?Tid=7709').read()
from bs4 import BeautifulSoup
soup = BeautifulSoup(source, features="lxml")

inputTags = soup.find('a', class_='item-rating')

print(inputTags["title"])