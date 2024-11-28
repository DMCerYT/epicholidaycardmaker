from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cards/', views.card_list, name="cards"),
    path('cards/<uuid:card_hash_id>', views.card_render, name="card_render"),
]