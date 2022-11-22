# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import os

class StampcollectorPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        os.makedirs("database", exist_ok=True)
        self.conn=sqlite3.connect("database/stamps.sqlite")
        self.curs=self.conn.cursor()

    def create_table(self):
        self.curs.execute("""drop table if exists stamp_table""")
        self.curs.execute("""create table stamp_table(
            section text,
            subsection_id text,
            origin_E text,
            origin_W text,
            end_E text,
            end_W text,
            distance text,
            time_E text,
            time_W text,
            elevation_E text,
            elevation_W text)
            """)
    def process_item(self, item, spider):

        self.store_db(item)
        return item

    def store_db(self, item):
        if len(item)>0:
            outp="(?"+", ?"*(len(item)-1)+")"
            self.curs.execute(f"""insert into stamp_table ({','.join([str(k) for k in item])}) values {outp}""", [str(v) for v in item.values()])
            self.conn.commit()