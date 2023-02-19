from django.urls import path
from .views import RequestListView, RequestCreateView

urlpatterns = [
    path('', RequestListView.as_view(), name = 'request list'),
    #path('<int:pk>/', ),
    path('create/', RequestCreateView.as_view(), name = 'request create'),
    #path('<int:pk>/delete/'),
    #path('<int:pk>/edit/'),
]
