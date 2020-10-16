import scrapy

class QuotesSpider(scrapy.Spider):
	name =  "recipes"

	def start_requests(self):
		urls = [
			'https://www.recipetineats.com/recipes/?fwp_paged=1'
		]

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("=")[-1]
		filename = f'recipes-{page}.html'
		with open(filename, 'wb') as f:
			for link in [link.attrib['href'] in response.css('.entry-title-link').getall():
				self.log("--------------------------")
				self.log(link)