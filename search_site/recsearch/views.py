from django.shortcuts import render
from django.http import HttpResponse
from .es_call import recsearch, recshow

def search_index(request):
	results = []
	search_terms = []

	i = 0;
	while i<10 and request.GET.get('ingr'+str(i)) != None:
		ingredient = request.GET.get('ingr' + str(i))
		print(ingredient)
		search_terms.append(ingredient)
		i+=1

	results = recsearch(rec_ingredients=search_terms)
	print(results)
	context = {'results': results, 'count': len(results), 'search_terms': search_terms}

	return render(request, 'recsearch/index.html', context)

def show_view(request,recipe_id):
	result = recshow(rec_id=recipe_id)
	context = result
	return render(request, 'recsearch/show.html', context)