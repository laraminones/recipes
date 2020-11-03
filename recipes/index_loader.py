import requests, json, os
from elasticsearch import Elasticsearch

# TODO - allow users to specify the index_file
index_filename = 'recipes.json'

# TODO - network and connection checks
res = requests.get('http://localhost:9200')
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

# ignore=400 to ignore Elastic format errors on json fields
with open(index_filename, "r") as index_file:
  i = 1
  for line in list(index_file):
    docket_content = line
    es.index(index='recipe_index', ignore=400, doc_type='docket', 
    id=i, body=docket_content)
    i = i + 1
