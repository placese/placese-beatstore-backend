from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from beatstore.models import Beat
from beatstore.serializers import BeatSerializer


class BeatViewSet(ModelViewSet):
    queryset = Beat.objects.all()
    serializer_class = BeatSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price_wav']
    search_fields = ['name']
    ordering_fields = ['price_wav', 'name']
