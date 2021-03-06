import requests, json, os
from elasticsearch import Elasticsearch

# TODO - allow users to specify the index_file
index_filename = 'recipes.jsonlines'

# TODO - network and connection checks
res = requests.get('http://localhost:9200')
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

# ignore=400 to ignore Elastic format errors on json fields
with open(index_filename, 'r') as index_file:
  rec_list = list(index_file)

recipes = [{key: json.loads(line)[key] for key in json.loads(line).keys()}
			 for line in rec_list]

doc = {
            "settings" : {
                "analysis" : {
                  "analyzer": {
                    "default": {
                      "tokenizer": "whitespace",
                      "filter": [ "lowercase", "stemmer" ]
                    }
                  }
                }
            },
              "mappings": {
		    "properties": {
		      "rec_cook_time": {
			"type": "text",
			"analyzer": "default",
		        "fields": {
		      	    "keyword": {
				"type": "keyword",
				"ignore_above": 256
		      	    }
		    	}
		      },
		      "rec_img": {
			"type": "text",
			"analyzer": "default",
		        "fields": {
		      	    "keyword": {
				"type": "keyword",
				"ignore_above": 256
		      	    }
		    	}
		      },
		      "rec_ingredients": {
			"type": "text",
			"analyzer": "default",
		        "fields": {
		      	    "keyword": {
				"type": "keyword",
				"ignore_above": 256
		      	    }
		    	}
		      },
		      "rec_instructions": {
			"type": "text",
			"analyzer": "default",
		        "fields": {
		      	    "keyword": {
				"type": "keyword",
				"ignore_above": 256
		      	    }
		    	}
		      },
		      "rec_prep_time": {
			"type": "text",
			"analyzer": "default",
		        "fields": {
		      	    "keyword": {
				"type": "keyword",
				"ignore_above": 256
		      	    }
		    	}
		      },
		      "rec_servings": {
			"type": "text",
			"analyzer": "default",
		        "fields": {
		      	    "keyword": {
				"type": "keyword",
				"ignore_above": 256
		      	    }
		    	}
		      },
		      "rec_title": {
			"type": "text",
			"analyzer": "default",
		        "fields": {
		      	    "keyword": {
				"type": "keyword",
				"ignore_above": 256
		      	    }
		    	}
		    }
		}
	}
}

es.index(index='recipe_index',body=doc)

i = 1
for rec in recipes:
	es.index(index='recipe_index', ignore=400, id=i, body=rec)
	i = i + 1
