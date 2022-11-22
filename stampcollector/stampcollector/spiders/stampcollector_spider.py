import scrapy
from ..items import StampcollectorItem
import json
import parse
import sys

table_cols=[
    "origin",
    "end",
    "distance",
    "time",
    "elevation",
]


class StampcollectorSpider(scrapy.Spider):
    name="stampcollector"

    start_urls=[rf"https://www.kektura.hu/okt-szakasz/okt-{section:02}" 
    for section in range(1,28)]

    def parse(self, response, **kwargs):

        tables=response.css("tbody")

        for i, row in enumerate(tables[1].css("tr")):
            item=StampcollectorItem()

            for col_name, cell in zip(table_cols,row.css("td")):
                print(col_name)
                if col_name == "distance":
                    int_part=int(cell.css("span.int-part::text").extract_first()) 
                    dec_part=0.1*int(cell.css("span.decimal-part::text").extract_first()) 
                    item[col_name]=int_part+dec_part

                else:
                    item[f"{col_name}_E"]=cell.css("::attr(data-oda)").extract_first()
                    item[f"{col_name}_W"]=cell.css("::attr(data-vissza)").extract_first()

            item["section"]=response.css(".col-md-4 h1::text").extract_first()
            item["subsection_id"]=i

            # print(item)
            yield item