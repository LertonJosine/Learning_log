from django.shortcuts import render
from learning_logs.models import Topic
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method == 'GET':
        form = EntryForm()
    elif request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {
        'form': form,
        'topic': topic
    }

    return render(request,'new_entry.html',context)


def new_topic(request):
    if request.method == 'GET':
        form = TopicForm()
    elif request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {
        'form': form
    }

    return render(request, 'new_topic.html', context)