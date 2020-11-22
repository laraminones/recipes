from django.urls import path 
from . import views 

app_name = 'recsearch' 
urlpatterns = [ 
path('', views.search_index, name='search_view'),
path('show/<int:recipe_id>', views.show_view, name='show_view') 
]