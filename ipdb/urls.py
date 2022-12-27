from django.urls import path, include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register("ipposts", views.IppostViewSet, 'ippost')
routers.register("iphomeposts", views.IphomepostViewSet, 'iphomepost')

urlpatterns = [
    path('', include(routers.urls)),
    # path('orders/', views.OrdersList.as_view())
]