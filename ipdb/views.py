from django.shortcuts import render
from .models import Ipdb, Iphomedb

# Create your views here.

from .serializers import *

from django.http import Http404
from django.conf import settings
from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics, status, permissions, authentication
from rest_framework.decorators import action
from rest_framework.response import Response

class IppostViewSet(viewsets.ViewSet):
    serializer_class = IpdbSerializer

    def get_queryset(self):
        cards = Ipdb.objects.all()
        q = self.request.query_params.get('q')
        if q is not None:
            cards = cards.filter(name__icontains=q)
        return cards

    @action(methods=['post'], detail=False, url_path="views")
    def inc_view(self, request):
        ipp = request.data['ip']
        postt = request.data['post']
        v, created = Ipdb.objects.get_or_create(post = postt, ip=ipp)
        v.sl += 1
        v.save()
        v.refresh_from_db()
        return Response(IpdbSerializer(v).data, status=status.HTTP_200_OK)
    
    @action(methods=['post'], detail=False, url_path="views_total")
    def get_inc_view(self, request):
        list_ip = Ipdb.objects.filter(post=request.data['post'])
        mydata = IpdbSerializer(list_ip, many = True)
        sum = 1
        for i in mydata.data:
            sum += i['sl']
        return Response(sum, status=status.HTTP_200_OK)
    

class IphomepostViewSet(viewsets.ViewSet):
    serializer_class = IphomedbSerializer

    def get_queryset(self):
        cards = Iphomedb.objects.all()
        q = self.request.query_params.get('q')
        if q is not None:
            cards = cards.filter(name__icontains=q)
        return cards
    @action(methods=['post'], detail=False, url_path="views")
    def inc_view_home(self, request):
        ipp = request.data['ip']
        v, created = Iphomedb.objects.get_or_create(ip = ipp)
        v.sl += 1
        v.save()
        v.refresh_from_db()
        return Response(IphomedbSerializer(v).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path="views_total")
    def get_total_view(self, request):
        list_ip = Iphomedb.objects.all()
        mydata = IphomedbSerializer(list_ip, many = True)
        sum = 1
        for i in mydata.data:
            sum += i['sl']
        return Response(sum, status=status.HTTP_200_OK)