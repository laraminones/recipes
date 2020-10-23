import scrapy

class QuotesSpider(scrapy.Spider):
	name =  "recipes"

	def __init__(self):
		self.page = 1
		self.url = 'https://www.recipetineats.com/recipes/?fwp_paged='

	def start_requests(self):		

		yield scrapy.Request(url=self.url+str(self.page), callback=self.parse)

	def parse(self, response):
		last = True
		for link in [link.attrib['href'] for link in response.css('.entry-title-link')]:
			last = False
			meta = {
				'recipe_url': link
			}
			yield scrapy.Request(url=link, callback=self.parse_recipe, meta=meta)

		if last == False:
			self.page+=1
			yield scrapy.Request(url=self.url+str(self.page), callback=self.parse)


	def parse_recipe(self, response):
		rec_title = response.css('.wprm-recipe-name::text')[0].get()
		rec_prep_time = response.css('.wprm-recipe-prep_time::text')[0].get()
		rec_cook_time = response.css('.wprm-recipe-cook_time::text')[0].get()
		#rec_servings = response.css('.wprm-recipe-servings::text')[0]
		rec_ingredients = response.css('.wprm-recipe-ingredient-name::text').getall()
		#rec_ingredients_amount = response.css('.wprm-recipe-ingredient-amount::text').getall()
		rec_instructions = response.css('.wprm-recipe-instruction-text *::text').getall()

		self.log(rec_title)
		self.log(rec_prep_time)
		self.log(rec_cook_time)
		self.log(rec_ingredients)
		self.log(rec_instructions)

		yield {
			'rec_title' : rec_title,
			'rec_prep_time' : rec_prep_time,
			'rec_cook_time' : rec_cook_time,
			'rec_ingredients' : rec_ingredients,
			'rec_instructions' : rec_instructions,
		}

