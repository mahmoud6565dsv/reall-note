
from django.urls import re_path as url
from . import views 


app_name = 'Note'
urlpatterns = [
    
    url(r'^$', views.all_notes , name='all_notes'),
    url(r'^(?P<slug>[-\w]+)/$', views.details, name='note_detail'),
    url(r'^add$', views.add_note , name='note_add'),
    url(r'^(?P<slug>[-\w]+)/comment$', views.add_Comment , name='add_Comment'),
    # url(r'(?P<slug>[-\w]+)/comment/<int:id>/delete/$', views.DeleteComment.as_view() , name='delete_comment'),
    url(r'^(?P<slug>[-\w]+)/edit$', views.edit, name='note_edit'),
    url(r'^(?P<slug>[-\w]+)/delete/$', views.Delete.as_view(), name='delete_note'),
]
