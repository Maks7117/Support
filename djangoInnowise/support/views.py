from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Ticket, User
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .tasks import *


# Create your views here.


class TicketCreateView(generics.CreateAPIView):
    serializer_class = TicketDetailSerializer




class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketDetailSerializer
    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated,)
    #permission_classes = (IsOwnerOrReadOnly,)


class TicketListView(generics.ListAPIView):
    serializer_class = TicketListSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

