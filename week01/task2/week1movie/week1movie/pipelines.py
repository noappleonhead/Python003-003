# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Week1MoviePipeline:
    def process_item(self, item, spider):
        movieName = item['movieName']
        movieType = item['movieType']
        releaseDate = item['releaseDate']
        output = f'{movieName},{movieType},{releaseDate}\n'
        with open('./movieTop10.csv','a+',encoding='utf-8') as article:
            article.write(output)
        return item
