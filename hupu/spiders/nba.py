import scrapy
from hupu.items import HupuItem
from lxml import etree

class Nba(scrapy.Spider):
    name = "nba"
    start_urls = [
        'https://nba.hupu.com/players/rockets'
    ]

    def parse(self, response):
        # page = etree.HTML(response.body.decode('utf-8'))
        # print("hahahahahah")
        # a= page.xpath('/html/body/div[3]/div[4]/table/tbody/tr[3]/td[2]/b/a/text()')
        # print(len(a))
        # with open('nba.txt','w') as f:
        #     f.write(a[0])
        # return
        # playerDiv = response.xpath("//table[@class='players_table']").extract()[0]
        # playerTd = etree.HTML(playerDiv).xpath("//tr")
        #
        # print(playerTd[1].xpath("*/text()"))
        # playerName = playerTd[1].xpath("//a/@href")
        #
        # print("__________")
        # print(etree.tostring(playerTd[1],encoding='utf-8').decode('utf-8'))
        #
        # print("________________")
        # print(playerName)
        # print(etree.tostring(playerName, encoding='utf-8').decode('utf-8'))
        item = HupuItem()
        item['name'] = response.xpath("//table[@class='players_table']/tbody/tr[2]/td[2]//a/text()").extract_first()
        item['number'] = response.xpath("//table[@class='players_table']/tbody/tr[2]/td[3]/text()").extract_first()
        item['height'] = response.xpath("//table[@class='players_table']/tbody/tr[2]/td[5]/text()").extract_first()
        item['born'] = response.xpath("//table[@class='players_table']/tbody/tr[2]/td[7]/text()").extract_first()
        item['contract'] = response.xpath("//table[@class='players_table']/tbody/tr[2]/td[8]/text()").extract_first()
        yield item



