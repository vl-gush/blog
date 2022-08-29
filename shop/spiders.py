import logging
import os

from decimal import Decimal

import requests
import scrapy

logger = logging.getLogger(__name__)


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    start_urls = ["https://www.oma.by/elektroinstrument-c"]

    def parse(self, response, **kwargs):
        for product in response.css(".catalog-grid .product-item"):
            try:
                cost = product.css(".product-price-block .price__normal::text").get().strip()
                cost = Decimal(cost.replace(",", "."))
            except Exception:
                cost = 0

            default_image = 'products/no-image.jpg'
            image = product.css(".product-item_img-box .catlg_list_img::attr(src)").get()
            image_name = os.path.split(image)[1]
            if image_name == "preloader_small.gif":
                image_path = default_image
            else:
                image_path = os.path.join('products', image_name)
                with open(os.path.join('media', image_path), 'wb') as img:
                    img.write(requests.get(f'http://{self.name}/{image}').content)

            data = {
                "external_id": product.attrib.get("data-ga-product-id"),
                "title": product.css(".product-title-and-rate-block .wrapper::text").get().strip(),
                "cost": cost,
                "link": f"https://www.oma.by{product.css('a.area-link::attr(href)').get()}",
                "image": image_path
            }
            yield data

        next_page = response.css(".page-nav_box .btn__nav-right::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
