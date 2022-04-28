"""Defines URL patterns for users"""

#from django.conf.urls import url
#from django.contrib.auth.views import login <<--Deprecated
#from django.contrib.auth.views import LoginView as login 
#from django.contrib.auth import views as auth_views

from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate

from . import views

app_name = 'users'

# urlpatterns = [
#     # Login page
#     url(r'^login/$', LoginView, {'template_name': 'users/login.html'}, name='login'), 
#     #path('login/', auth_views.LoginView.as_view(), name='login')
#     # Logout page
#     url(r'^logout/$', views.logout_view, name='logout'),
    
#     # Registration page
#     url(r'^register/$', views.register, name='register'),
# ]

urlpatterns = [
    # Login page.
    path('login/',
    auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout page.
    #path('logout/', views.logout_view, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Registration page.
    path('register/', views.register, name='register')
]