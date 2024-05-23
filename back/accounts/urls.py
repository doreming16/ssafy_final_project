from django.urls import path
from . import views

# app_name = 'accounts'

urlpatterns = [
    # path('', views.index),
    path('api/submit-form/', views.submit_form, name='submit_form'),
    path('api/userinfo/', views.get_userinfo_list, name="userinfo_list"),
    path('profile/', views.get_user_profile, name='user-profile'),
]