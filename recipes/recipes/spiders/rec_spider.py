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
		for link in [link.attrib['href'] for link in response.css('.entry-title-link')]:
			meta = {
				'recipe_url': link
			}
			yield scrapy.Request(url=link, callback=self.parse_recipe, meta=meta)

	def parse_recipe(self, response):
		rec_title = response.css('.wprm-recipe-name::text')[0]
		rec_prep_time = response.css('.wprm-recipe-prep_time::text')[0]
		rec_cook_time = response.css('.wprm-recipe-cook_time::text')[0]
		#rec_servings = response.css('.wprm-recipe-servings::text')[0]
		rec_ingredients = response.css('.wprm-recipe-ingredient-name::text').getall()
		#rec_ingredients_amount = response.css('.wprm-recipe-ingredient-amount::text').getall()
		rec_instructions = response.css('.wprm-recipe-instruction-text > span::text').getall()

		self.log(rec_title)
		self.log(rec_prep_time)
		self.log(rec_cook_time)
		self.log(rec_ingredients)
		self.log(rec_instructions)

