from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail, name='index'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('index_01/', views.index_01, name='index_01'),
    path('detail_01/<int:question_id>', views.detail_01, name='detail_01'),
    path('detail_02/<int:question_id>', views.detail_02, name='detail_02'),
    path('detail_03/', views.detail_03, name='detail_03'),
    path('detail_04/<int:question_id>/', views.detail_04, name='detail_04'),
]