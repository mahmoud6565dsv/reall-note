
from django.urls import re_path as url
from . import views
# from django.contrib.auth.views import login , logout
# from django.contrib.auth.views import LoginView ,LoginView
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import login , logout
app_name = 'accounts'
urlpatterns = [
    
    url(r'^$', views.home , name='home'),
    # url(r'^login/$', login,{'template_name': 'login.html'}, name = 'login'),
    url('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url('logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.register , name='register'),
    url(r'^(?P<slug>[-\w]+)/$', views.profile  , name='profile'),
    url(r'^(?P<slug>[-\w]+)/edit$', views.edit_profile  , name='edit_profile'),
    url(r'^(?P<slug>[-\w]+)/change_password$', views.change_password  , name='change_password'),
]

