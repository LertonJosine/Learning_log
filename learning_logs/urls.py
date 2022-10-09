from learning_logs.views import home, topics, topic, new_topic, new_entry
from django.urls import path

urlpatterns = [
    path('', home, name='index'),
    path('topics/', topics, name='topics'),
    path('topics/<int:topic_id>/', topic, name='topic'),
    path('new_topic/', new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', new_entry, name='new_entry')

]
