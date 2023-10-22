from django.urls import path
from crawled_data import views

urlpatterns = [
    path('', view=views.score_board, name='')
]