# config/urls.py
from django.urls import path
from .views import EventsListView,EventsUpdateView,EventsDeleteView,EventsDetailView,EventsCreateView

urlpatterns = [
    path('', EventsListView.as_view(),name='events_list'), # new
    path('<int:pk>/edit', EventsUpdateView.as_view(),name='events_edit'), # new
    path('<int:pk>/delete', EventsDeleteView.as_view(),name='events_delete'), # new
    path('<int:pk>/', EventsDetailView.as_view(),name='events_detail'), # new
    path('new/', EventsCreateView.as_view(),name='events_new'), # new
]