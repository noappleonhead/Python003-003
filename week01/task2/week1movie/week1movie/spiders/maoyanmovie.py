import scrapy
from scrapy.selector import Selector
from week1movie.items import Week1MovieItem

class MaoyanmovieSpider(scrapy.Spider):
    name = 'maoyanmovie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        yield scrapy.Request(url='https://maoyan.com/films?showType=3', callback=self.parse1)

    def parse1(self, response):
        topMovies = Selector(response=response).xpath(
            '//div[@class="channel-detail movie-item-title"]')[:10]
        for movie in topMovies:
            movie_url = 'https://maoyan.com' + \
                movie.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=movie_url, callback=self.parse2)

    def parse2(self, response):

        item = Week1MovieItem()

        # name 
        movieName = Selector(response=response).xpath(
            '//h1[@class="name"]/text()').extract_first()

        # type 
        types = []
        for mtype in Selector(response=response).xpath('//a[@class="text-link"]/text()').extract():
            types.append(mtype.strip())
        movieType = '/'.join(types)

        # release date
        releaseDate = Selector(response=response).xpath(
            '//li[@class="ellipsis"][3]/text()').extract_first()[:10]

        item['movieName'] = movieName
        item['movieType'] = movieType
        item['releaseDate'] = releaseDate
        return item
