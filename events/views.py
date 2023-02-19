from .models import Events
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import (
LoginRequiredMixin,
UserPassesTestMixin # new
)

class EventsListView(LoginRequiredMixin, ListView):
    model=Events
    template_name="events_list.html"

class EventsDetailView(LoginRequiredMixin, DetailView):  # new
    model = Events
    template_name = 'events_detail.html'

class EventsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
    model = Events
    fields = ('name', 'link','location','modes') # new
    template_name = 'events_edit.html'

    def test_func(self): # new
        obj = self.get_object()
        return obj.posted_by == self.request.user

class EventsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Events
    template_name = 'events_delete.html'
    success_url = reverse_lazy('events_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.posted_by == self.request.user


class EventsCreateView(LoginRequiredMixin, CreateView): # new
    model = Events
    template_name = 'events_new.html'
    fields = ('name', 'link','location','modes') # new

    def form_valid(self, form): # new
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
