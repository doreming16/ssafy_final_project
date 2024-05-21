from django.urls import path
from . import views

# app_name = 'accounts'

urlpatterns = [
    # path('', views.index),
    # path('login/', views.login),
    # path('signup/', views.signup),
    # path('userinfo/', views.submit_form),
    path('api/submit-form/', views.submit_form, name='submit_form'),
    # path('userinfo/create', views.userinfo),
    # path('userinfo/edit', views.userinfo),
]