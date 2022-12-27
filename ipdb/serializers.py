from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from .models import Ipdb, Iphomedb

class IpdbSerializer(ModelSerializer):
    class Meta:
        model = Ipdb
        fields = ["ip", "post","sl"]

class IphomedbSerializer(ModelSerializer):
    class Meta:
        model = Iphomedb
        fields = ["ip", "sl"]