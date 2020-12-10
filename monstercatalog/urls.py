from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('monster/<int:monster_id>', views.monster_detail, name='monster_detail'),
    path('thesis/<int:thesis_id>', views.thesis_detail, name='thesis_detail'),
    path('thesis/comparison', views.thesis_comparison, name='thesis_comparison'),
]

