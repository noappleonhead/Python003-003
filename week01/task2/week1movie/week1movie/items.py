# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Week1MovieItem(scrapy.Item):
    movieName = scrapy.Field()
    movieType = scrapy.Field()
    releaseDate = scrapy.Field()
