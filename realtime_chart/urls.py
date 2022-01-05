from django.urls import path
from . import views

urlpatterns = [
    path('epochjs/', views.epochjs, name='chart'),
    path('webglplot/', views.webglplot, name='chart'),
]