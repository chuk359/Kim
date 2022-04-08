import django_filters.rest_framework
from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Table
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import TableSerializer


# Create your views here.

class TableAPIListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class TableAPIList(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = TableAPIListPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ['employment_position','parent']

class TableAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )


class TableAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = (IsAdminOrReadOnly, )

    


