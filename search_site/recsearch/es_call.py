from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.query import Query
from elasticsearch_dsl.query import MultiMatch, Match

def recsearch(rec_ingredients=""):
    client = Elasticsearch()
    q = Q('bool', must=[Q('term', rec_ingredients=rec_ingredients)])
    s = Search(index="recipe_index").using(client).query(q) 
    response = s.execute()
    search = get_results(response)
    return search

def get_results(response):
    results = []
    for hit in response:
        results.append([hit.rec_title,
            hit.rec_prep_time,
            hit.rec_cook_time,
            hit.rec_ingredients,
            hit.rec_instructions])
    return results

if __name__ == '__main__':  
    found = recsearch(rec_ingredients = "salt")
    print("rec_prep_time 20 details:\n")
    for f in found:
    	print(f)
