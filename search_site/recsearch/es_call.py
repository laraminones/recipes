from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

def recsearch(rec_prep_time=""):
    client = Elasticsearch()
    q = Q("match", rec_prep_time=rec_prep_time)
    s = Search(index="recipe_index").using(client).query(q)
    response = s.execute()
    search = get_results(response)
    return search

def get_results(response):
    results = []
    for hit in response:
        results.append([hit.rec_title, hit.rec_prep_time])
    return results

if __name__ == '__main__':  
    print("rec_prep_time 20 details:\n", recsearch(rec_prep_time = "20"))
