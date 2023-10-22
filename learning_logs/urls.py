"""
Определяет схемы URL для learning_logs
"""

from django.urls import path

from learning_logs.views import index, topics, topic

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', index, name='index'),
    # Страница со списком всех тем
    path('topics/', topics, name = 'topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>', topic, name = 'topic'),
]

