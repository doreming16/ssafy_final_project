from django.urls import path
from . import views

# app_name = 'accounts'

urlpatterns = [
    path('api/submit-form/', views.submit_form, name='submit_form'),
    path('api/userinfo/', views.get_userinfo_list, name="userinfo_list"),
    
    # path('', views.index),
    # path('userinfo/', views.submit_form),
    # path('userinfo/create', views.userinfo),
    # path('userinfo/edit', views.userinfo),
]