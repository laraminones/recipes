from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.query import Query
from elasticsearch_dsl.query import MultiMatch, Match

def recshow(rec_id):
    client = Elasticsearch()
    q = Q('term', _id= rec_id)
    s = Search(index="recipe_index").using(client).query(q)
    response= s.execute()
    show = get_show_result(response)
    return show

def get_show_result(response):
    hit = response[0]
    result = {'title': hit.rec_title,
        'prep_time': hit.rec_prep_time,
        'cook_time': hit.rec_cook_time,
        'ingredients': hit.rec_ingredients,
        'instructions': hit.rec_instructions,
        'servings': hit.rec_servings,
        'img': hit.rec_img}
    return result

def recsearch(rec_ingredients=""):
    client = Elasticsearch()
    q = Q('bool', must=[Q('term', rec_ingredients=rec_ingredients)])
    s = Search(index="recipe_index").using(client).query(q) 
    response = s.execute()
    search = get_search_results(response)
    return search

def get_search_results(response):
    results = []
    for hit in response:
        results.append([hit.rec_title,
            hit.rec_prep_time,
            hit.rec_cook_time,
            hit.rec_ingredients,
            hit.rec_instructions,
            hit.rec_servings,
            hit.rec_img,
            hit.meta.id])
    return results

if __name__ == '__main__':  
    found = recsearch(rec_ingredients = "salt")
    print("rec_prep_time 20 details:\n")
    for f in found:
    	print(f)
