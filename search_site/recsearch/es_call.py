from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.query import Query
from elasticsearch_dsl.query import MultiMatch, Match
import functools

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

def recsearch(rec_ingredients=[]):
    client = Elasticsearch()
    q = Q('bool', must=[Q('term', rec_ingredients=ingr) for ingr in rec_ingredients])
    s = Search(index="recipe_index").using(client).query(q)
    s = s[0:s.count()] 
    response = s.execute()
    search = get_search_results(response)
    return search

def get_search_results(response):
    results = []
    for hit in response:
        results.append({
            'title' : hit.rec_title,
            'prep_time': hit.rec_prep_time,
            'cook_time': hit.rec_cook_time,
            'summary': get_summary(hit.rec_instructions),
            'servings': hit.rec_servings,
            'img': hit.rec_img,
            'id': hit.meta.id})
    return results

def get_summary(instructions):
    left = 250
    i = 0
    summary = ""
    while left>0 and i<len(instructions)-1:
        instr = instructions[i]
        to_add = (len(instr) if left > len(instr) else left )
        summary += " "+instr[0:to_add]
        left -= to_add
        i += 1
    return summary + "..."
    

if __name__ == '__main__':  
    found = recsearch(rec_ingredients = "salt")
    print("rec_prep_time 20 details:\n")
    for f in found:
    	print(f)
