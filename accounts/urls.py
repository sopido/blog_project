from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),# www.ali_blog.com/accounts/login
    path('register', views.register, name='register'),# www.ali_blog.com/accounts/register
    path('logout', views.logout, name='logout'),  # www.ali_blog.com/accounts/loguot
]