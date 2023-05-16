#Implement Spiders
- What to crawl: URLs start with start_requests() method.
- How to crawl: Callback function inputs web page and outputs Items, Requests etc.
- How to parse: Selectors which determine which parts of webpage are processed.

#Project 02
- Crawl data from website 
- Crawl all products (about 100 pages) in category url [GPU VIDEO GRAPHICS CARDS](https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-9?Tid=7709)

#Script

```
//Setup

```
//Python 3.10.11
pip install Scrapy, urllib, re, mysql.connector,
```
//Run to crawl
scrapy crawl GpusVideoGraphicsCards
```
```
//Run to crawl and store in csv file
scrapy crawl GpusVideoGraphicsCards -o GpusVideoGraphicsCards.csv -t csv
```


