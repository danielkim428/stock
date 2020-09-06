import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    COUNT_MAX = 1
    count = 0

    def start_requests(self):
        url = 'https://www.investing.com/equities/'
        tag = getattr(self, 'tag', None)

        if tag is not None:
            if (tag == 'apple'):
                tag = 'apple-computer-inc';
            url = url + tag + '-news'
        yield scrapy.Request(url, self.parse)

    #def parse(self, response):
    #    container = response.css('section#leftColumn')
    #    for article in container.css('div.mediumTitle1 article'):
    #        yield {
    #            'title': article.css('div.textDiv a.title::text').get()
    #        }

        #yield from response.follow_all(css='div.sideDiv a::attr(href)', callback=self.parse)

    def parse(self, response):
        for article in response.css('section#leftColumn div.mediumTitle1 article'):
            yield {
                'name': article.css('div.textDiv a.title::text').get(),
                'author': article.css('span.articleDetails span::text').get(),
            }

        links = response.css('section#leftColumn div.mediumTitle1 article a.title')
        yield from response.follow_all(links, self.parse_articles)

        self.count += 1

        if (self.count < self.COUNT_MAX):
            yield from response.follow_all(css='div.sideDiv a::attr(href)', callback=self.parse)

    def parse_articles(self, response):

        yield {
            'title': response.css('h1::text').get().strip(),
            'content': response.css('p::text').getall(),
        }
