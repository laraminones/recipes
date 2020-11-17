from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q, A
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
    serv_a = A('terms', field='rec_servings.keyword').metric("top_hit_all","top_hits",size=s.count())
    s.aggs.bucket('rec_servings_terms',serv_a)
    response = s.execute()

    search = get_search_results(response)
    return search,s.count()

def get_search_results(response):
    results = {}
    for group in response.aggregations.rec_servings_terms.buckets:
        key = group.key
        count = group.doc_count
        results[key]=({'count': count, 'docs': []})
        for doc in group.top_hit_all.hits:
            results[key]['docs'].append({
                'title' : doc.rec_title,
                'prep_time': doc.rec_prep_time,
                'cook_time': doc.rec_cook_time,
                'summary': get_summary(doc.rec_instructions),
                'servings': doc.rec_servings,
                'img': doc.rec_img,
                'id': doc.meta.id})
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
    found = recsearch(rec_ingredients = ["bacon"])
    print("rec_prep_time 20 details:\n")
    for f in found:
    	print(found[f])
