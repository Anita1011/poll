from django.forms import ModelForm

from .models import Poll
from django import forms
from django.contrib.auth.models import User

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']

