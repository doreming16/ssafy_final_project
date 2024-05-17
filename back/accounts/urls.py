from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('login/', views.login),
    path('signup/', views.signup),
    path('userinfo/', views.userinfo),
    path('userinfo/create', views.userinfo),
    path('userinfo/edit', views.userinfo),
]