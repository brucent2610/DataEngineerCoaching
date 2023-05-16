import scrapy
import re

from SimpleSpiders.items import GpuVideoGraphicItem
from scrapy.loader import ItemLoader

class GpusvideographicscardsdetailSpider(scrapy.Spider):
    name = "GpusVideoGraphicsCardsDetail"
    allowed_domains = ["www.newegg.com"]
    start_urls = ["https://www.newegg.com/gigabyte-geforce-rtx-4070-gv-n4070wf3oc-12gd/p/N82E16814932611"]

    def __init__(self, filename=None):
        if filename:
            with open(filename, 'r') as f:
                self.start_urls = f.readlines()

    def parse(self, response):

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
                
        item_loader = ItemLoader(item = GpuVideoGraphicItem())
        item_loader.add_value("item_id", response.url)

        item = item_loader.load_item()
        item["others"] = {
            "MaxResolution": max_resolution,
            "DisplayPort": display_port,
            "HDMI": hdmi,
            "DirectX": direct_x,
            "Model": model
        }

        yield item
