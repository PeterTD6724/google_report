from django.urls import path,include
from . import views
# from django.urls import re_path
from django.urls import re_path as url


# urlpatterns = [
#     re_path(r'check/',views.check,name='check'),
# ]


urlpatterns = [
    url(r'check/', views.check, name='check'),
]

urlpatterns =[
    path(r'', views.home, name='home'),
    path(r'postsign/', views.postsign),
    path(r'signin/', views.signin, name="signin"),
    path(r'logout/', views.logout, name="log"),
    path(r'signup/', views.signUp, name="signup"),
    path(r'postsignup/', views.postsignup, name="postsignup"),
    path(r'create/', views.create, name="create"),
    path(r'post_create/', views.post_create, name="post_create"),
    path(r'check/', views.check, name="check"),
    path(r'post_check/', views.post_check, name="post_check"),
]