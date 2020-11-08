from django.shortcuts import render
from django.http import HttpResponse
from .es_call import recsearch

def search_index(request):
	results = []
	rec_ingredients_term = ""

	if request.GET.get('rec_ingredients'):
		rec_ingredients_term = request.GET['rec_ingredients']

	search_term = rec_ingredients_term
	results = recsearch(rec_ingredients=rec_ingredients_term)
	print(results)
	context = {'results': results, 'count': len(results), 'search_term': search_term}

	return render(request, 'recsearch/index.html', context)
