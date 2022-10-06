from learning_logs.views import home, topics, topic
from django.urls import path

urlpatterns = [
    path('', home, name='index'),
    path('topics/', topics, name='topics'),
    path('topics/<int:topic_id>/', topic, name='topic'),

]
