from django.urls import path
from . import views
from .views import ImagePathView

urlpatterns = [
    # path('', views.index),
    # path('recommend/', views.index),
    # path('recommend/', views.index),
    # path('<int:pk>/', views.detail),
    # path('<int:pk>/rate/', views.rate),
    # path('<int:pk>/rate/edit', views.rate),
    # path('<int:pk>/rate/delete', views.rate),
    path('detail/<int:pk>/review/', views.review, name='review'),
    path('api/image-paths/', ImagePathView.as_view(), name='image-paths'),
]