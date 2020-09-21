from django.urls import path

from . import views

urlpatterns = [
    path('', views.read, name='read'),
    path('create', views.create, name='create'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
]
