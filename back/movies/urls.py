from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('recommend/', views.index),
    # path('recommend/', views.index),
    path('<int:pk>/', views.detail),
    path('<int:pk>/rate/', views.rate),
    path('<int:pk>/rate/edit', views.rate),
    path('<int:pk>/rate/delete', views.rate),
]