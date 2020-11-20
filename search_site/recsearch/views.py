from django.shortcuts import render
from django.http import HttpResponse
from .es_call import recsearch, recshow

def search_index(request):
	results = []
	search_terms = []

	i = 0;
	while i<10:
		ingredient = request.GET.get('ingr' + str(i))
		if ingredient !=  None:
			print(ingredient)
			search_terms.append(ingredient)
		i+=1

	results = recsearch(rec_ingredients=search_terms)
	print(results[2])
	context = {'results': results[0], 'count': results[1], 'ingr_hints': results[2], 'search_terms': search_terms}

	return render(request, 'recsearch/index.html', context)

def show_view(request,recipe_id):
	result = recshow(rec_id=recipe_id)
	context = result
	return render(request, 'recsearch/show.html', context)