import scrapy
import json


class ProductSpider(scrapy.Spider):
    name = 'product_spider'
    start_urls = [
        'https://www.nordstrom.com/browse/men/shoes/boots?breadcrumb=Home%2FMen%2FShoes%2FBoots&origin=topnav',
        'https://www.zappos.com/men-sandals/CK_XARC51wHAAQLiAgMBAhg.zso?s=bestForYou/desc'
    ]

    def parse(self, response):
        # 解析列表页
        products = response.css('.product-card')
        for product in products:
            title = product.css('.product-title a::text').get()
            price = product.css('.price::text').get()
            color = product.css('.color::text').get()
            size = product.css('.size::text').get()
            sku = product.css('.sku::text').get()
            details = product.css('.details::text').get()
            img_urls = product.css('.product-image img::attr(src)').getall()

            # 构造商品信息字典
            item = {
                'title': title,
                'price': price,
                'color': color,
                'size': size,
                'sku': sku,
                'details': details,
                'img_urls': img_urls
            }
            yield item

    def closed(self, reason):
        # 在爬虫关闭时保存为JSON文件
        filename = 'result.json'
        with open(filename, 'w') as f:
            json.dump(self.items, f)


