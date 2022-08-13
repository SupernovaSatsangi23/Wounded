from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # 'home/'

    path('human/', views.human, name='human'),
    path('animal/', views.animal, name='animal'),

    path('human_disease_archive/', views.human_disease_archive, name='human_disease_archive'),
    path('human_injury_archive/', views.human_injury_archive, name='human_injury_archive'),
    path('human_psychology_archive/', views.human_psychology_archive, name='human_psychology_archive'),

    path('animal_disease_archive/', views.animal_disease_archive, name='animal_disease_archive'),
    path('animal_injury_archive/', views.animal_injury_archive, name='animal_injury_archive'),

    path('facts_archive/', views.facts_archive, name='facts_archive'),
    path('products/', views.products, name='products'),
    path('onlinesale/', views.onlinesale, name='onlinesale'),

    path('checkout/', views.checkout, name='checkout'),
]