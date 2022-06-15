from django.shortcuts import render
from rest_framework import generics
from .serializers import TicketListSerializer, TicketDetailSerializer
from .models import Ticket, User
from rest_framework.permissions import IsAuthenticated, IsAdminUser



# Create your views here.


class TicketCreateView(generics.CreateAPIView):
    serializer_class = TicketDetailSerializer
    permission_classes = (IsAuthenticated, )



class TicketListView(generics.ListAPIView):
    serializer_class = TicketListSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser, )

