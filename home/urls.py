
from django.urls import re_path as url
from . import views

app_name = 'home'
urlpatterns = [
    
    url(r'^$', views.allnotes , name='all_notes'),

]