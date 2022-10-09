from django import forms
from django.forms import ModelForm
from learning_logs.models import Topic,Entry



class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields =  ['text']
        labels = {'text': ''}


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['texto']
        labesl = {'texto': ''}
        widget = {'texto': forms.Textarea(attrs={'cols':80})}
