import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from qnbfinansbank.items import Article


class QnbSpider(scrapy.Spider):
    name = 'qnb'
    allowed_domains = ['qnbfinansbank.com']
    start_urls = ['https://www.qnbfinansbank.com/qnb-finansbanki-taniyin/duyurular']

    def parse(self, response):
        links = response.xpath('//a[@class="news-results-title"]/@href').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//h1/text()').get().strip()
        content = response.xpath('//div[@class="page-subpage-content"]/p//text()').getall()
        date = content.pop(0).strip()
        date = datetime.strptime(date, '%d.%m.%Y')
        date = date.strftime('%Y/%m/%d')
        content = "\n".join(content)

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
