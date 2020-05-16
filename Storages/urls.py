from django.urls import path
from . import views


urlpatterns = [
path('', views.gallery, name='gallery'),
path('like/', views.like, name="like"),
path('dislike/', views.dislike, name="dislike"),
]
