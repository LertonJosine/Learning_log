from django.shortcuts import render
from learning_logs.models import Topic

# Create your views here.

def home(Request):
    return render(Request, 'index.html')


def topics(request):
    topics = Topic.objects.all()
    context = {
        'topics': topics
    }

    return render(request, 'topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.all()
    context = {
        'topic': topic,
        'entries': entries
    }

    return render(request, 'topic.html', context)