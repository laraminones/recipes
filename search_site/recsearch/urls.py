from django.urls import path 
from . import views 

app_name = 'recsearch' 
urlpatterns = [ 
path('', views.search_index, name='search_view'),
path('index.html', views.search_index, name='search_view'),
path('show.html', views.show_view, name='show_view') 
]