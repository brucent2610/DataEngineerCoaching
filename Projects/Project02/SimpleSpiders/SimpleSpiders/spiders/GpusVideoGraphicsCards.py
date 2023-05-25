import scrapy
import re

from SimpleSpiders.items import GpuVideoGraphicItem
from scrapy.loader import ItemLoader

class GpusvideographicscardsSpider(scrapy.Spider):
    name = "GpusVideoGraphicsCards"
    allowed_domains = ["www.newegg.com"]
    start_urls = [
        "https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-1?Tid=7709"
    ]

    def __init__(self, pages="1,100"):
        rangePages = pages.split(",")
        for i in range(int(rangePages[0]), int(rangePages[1]) + 1):
            list_url = "https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-"+ str(i) +"?Tid=7709"
            print(list_url)
            self.start_urls.append(list_url)

    def parse_detail(self, response, item):

        max_resolution = ""
        display_port = ""
        hdmi = ""
        direct_x = ""
        model = ""

        product_details = response.css("#product-details .tab-panes")

        for table_horizontal in product_details.css(".tab-pane:nth-child(2) .table-horizontal"):
            if(table_horizontal.css("caption::text").extract_first() == "Model"):
                tr = table_horizontal.css("tbody tr")
                for r in tr:
                    th = r.css("th::text").extract_first()
                    if(th == "Model"):
                        td = r.css("td::text").extract_first()
                        model = td

            elif(table_horizontal.css("caption::text").extract_first() == "Ports"):
                tr = table_horizontal.css("tbody tr")
                for r in tr:
                    th = r.css("th::text").extract_first()
                    if(th == "DisplayPort"):
                        td = r.css("td::text").extract_first()
                        display_port = td
                    if(th == "HDMI"):
                        td = r.css("td::text").extract_first()
                        hdmi = td

            elif(table_horizontal.css("caption::text").extract_first() == "3D API"):
                tr = table_horizontal.css("tbody tr")
                for r in tr:
                    th = r.css("th::text").extract_first()
                    if(th == "DirectX"):
                        td = r.css("td::text").extract_first()
                        direct_x = td

            elif(table_horizontal.css("caption::text").extract_first() == "Details"):
                tr = table_horizontal.css("tbody tr")
                for r in tr:
                    th = r.css("th::text").extract_first()
                    if(th == "Max Resolution"):
                        td = r.css("td::text").extract_first()
                        max_resolution = td
            
            else:
                continue
                
            

        item["others"] = {
            "MaxResolution": max_resolution,
            "DisplayPort": display_port,
            "HDMI": hdmi,
            "DirectX": direct_x,
            "Model": model
        }

        yield item


    def parse(self, response):

        for item in response.css(".item-cell"):

            detail_url = item.css(".item-title::attr(\"href\")").extract_first()

            price = item.css(".price-current strong::text").extract_first()
            price_decimal = item.css(".price-current sup::text").extract_first()

            price_current = "0"
            if(price and price_decimal):
                price_current = re.sub("\D","",price) + price_decimal

            item_loader = ItemLoader(item = GpuVideoGraphicItem(), selector=item)
            item_loader.add_css("item_id", ".item-title::attr(\"href\")")
            item_loader.add_css("title", ".item-title::text")
            item_loader.add_css("brand", ".item-brand img::attr(\"title\")")
            item_loader.add_css("price_shipping", ".price-ship::text")
            item_loader.add_css("rating", "a.item-rating::attr(\"title\")")
            item_loader.add_css("rating_num", "a.item-rating .item-rating-num::text")
            item_loader.add_css("image_url", ".item-img img::attr(\"src\")")
            item_loader.add_value("price", price_current)
            item_loader.add_value("url", detail_url)
            item_loader.add_value("referer", response.url)

            # yield item_loader.load_item()
            yield scrapy.Request(detail_url, callback=self.parse_detail, cb_kwargs=dict(item=item_loader.load_item()))
            
        # Collect pagination to get current page
        # CURRENT_SELECTOR = ".list-tool-pagination .btn-group .btn-group-cell .is-current::text"
        # current_page = response.css(CURRENT_SELECTOR).extract_first()
        # if current_page:
        #     next_page = int(current_page) + 1

        #     print("Run next page: %s -> %s", current_page, next_page)

        #     yield scrapy.Request("https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-"+ str(next_page) +"?Tid=7709")
