import requests, json, os
from elasticsearch import Elasticsearch

# TODO - allow users to specify the index_file
index_filename = 'recipes.json'

# TODO - network and connection checks
res = requests.get('http://localhost:9200')
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

# ignore=400 to ignore Elastic format errors on json fields
with open(index_filename, 'r') as index_file:
  rec_list = list(index_file)

recipes = [{key: json.loads(line)[key] for key in json.loads(line).keys()}
			 for line in rec_list]

i = 1
for rec in recipes:
	es.index(index='recipe_index', ignore=400, id=i, body=rec)
	i = i + 1
