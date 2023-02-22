from .import views
from django.urls import path

app_name='Searchapp'

urlpatterns=[
    path('',views.SearchResult,name='SearchResult'),
]