from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import CollabRequestPost

class RequestListView(ListView):
    model = CollabRequestPost
    template_name = 'requests.html'

class RequestCreateView(CreateView):
    model = CollabRequestPost
    template_name = 'create_request.html'
    fields = ['title', 'team_size', 'description', 'author']
