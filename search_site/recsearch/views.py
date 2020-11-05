from django.shortcuts import render
from django.http import HttpResponse
from .es_call import recsearch

def search_index(request):
	results = []
	rec_prep_time_term = ""

	if request.GET.get('rec_prep_time'):
		rec_prep_time_term = request.GET['rec_prep_time']

	search_term = rec_prep_time_term
	results = recsearch(rec_prep_time=rec_prep_time_term)
	print(results)
	context = {'results': results, 'count': len(results), 'search_term': search_term}

	return render(request, 'recsearch/index.html', context)
