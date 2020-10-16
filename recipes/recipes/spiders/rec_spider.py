import scrapy

class QuotesSpider(scrapy.Spider):
	name =  "recipes"

	def start_requests(self):
		urls = [
			'https://es.wikipedia.org/wiki/Wikipedia:Portada'
		]

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = f'recipes-{page}.html'
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.flog(f'saved file {filename}')