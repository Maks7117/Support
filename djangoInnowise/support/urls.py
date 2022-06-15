from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('ticket/create', TicketCreateView.as_view()),
    path('users', TicketListView.as_view()),
   # path('detail/<int:pk>', TicketDetailView.as_view()),

]
