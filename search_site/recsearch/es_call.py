from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

def recsearch(rec_prep_time=""):
    client = Elasticsearch()
    #q = Q("bool", should=Q("match", rec_prep_time=rec_prep_time), minimum_should_match=1)
    q = Q("match", rec_prep_time='20')
    s = Search(index="recipes_index").using(client)#.query(q)
    response = s.execute()
    print('Total %s hits found.' % response.hits.total.value)
    search = get_results(response)
    return search

def get_results(response):
    results = []
    for hit in response:
        results.append(hit.rec_title)
    return results

if __name__ == '__main__':  
    print("rec_prep_time 20 details:\n", recsearch(rec_prep_time = "20"))