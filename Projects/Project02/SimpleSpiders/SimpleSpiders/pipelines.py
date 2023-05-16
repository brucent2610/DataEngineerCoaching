# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class SimplespidersPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'root',
            database = 'de_project2'
        )

        ## Create cursor, used to execute commands
        self.cur = self.conn.cursor()

        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS products(
            item_id VARCHAR(255) NOT NULL,
            title VARCHAR(255),
            brand VARCHAR(255),
            rating FLOAT,
            rating_num FLOAT,
            price FLOAT,
            price_shipping FLOAT,
            price_total FLOAT,
            image_url TEXT,
            url TEXT,
            referer TEXT,
            others TEXT,
            PRIMARY KEY (item_id)
        )
        """)

    def process_item(self, item, spider):

        print(item)

        ## Define insert statement
        item = dict(item)

        ## Check to see if text is already in database 
        self.cur.execute("select * from products where item_id = %s", (item['item_id'],))
        result = self.cur.fetchone()

        addtional_information = ""
        if('others' in item):
            addtional_information = str(item["others"])

        ## If it is in DB, create log message
        if result:
            spider.logger.warn("Item already in database: %s" % item['item_id'])

            self.cur.execute(""" 
                UPDATE products
                SET others = %s
                WHERE item_id = %s;
                """, (
                addtional_information,
                item["item_id"],
            ))

            self.conn.commit()

            spider.logger.warn("Item updated in database: %s" % item['item_id'])

        else:
            price_total = 0.0
            if('price' in item and 'price_shipping' in item): 
                price_total = item["price"] + item["price_shipping"]

            self.cur.execute(""" INSERT INTO products (
                item_id, 
                title, 
                brand, 
                rating, 
                rating_num, 
                price, 
                price_shipping, 
                price_total, 
                image_url, 
                url, 
                referer, 
                others) VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s)""", (
                item["item_id"],
                item["title"] if 'title' in item else "",
                item["brand"] if 'brand' in item else "",
                item["rating"] if 'rating' in item else 0,
                item["rating_num"] if 'rating_num' in item else 0,
                item["price"] if 'price' in item else 0,
                item["price_shipping"] if 'price_shipping' in item else 0,
                price_total,
                item["image_url"] if 'image_url' in item else "",
                item["url"] if 'url' in item else "",
                item["referer"] if 'referer' in item else "",
                addtional_information,
            ))

            ## Execute insert of data into database
            self.conn.commit()

            spider.logger.warn("Item created in database: %s" % item['item_id'])

    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.conn.close()
