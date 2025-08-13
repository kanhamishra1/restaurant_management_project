from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Item
from .serializers import ItemSerializer


def home(request):
    return render(request, 'products/home.html')
# '''
# NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
# '''

# # Create your views here.
# class ItemView(APIView):

#     def get(self, request):
#         items = Item.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def menu_items_view(request):
    
    menu_items = [
        {"name" : "Veg Burger", "price": 120},
        {"name" : "Paneer Pizza", "price": 250},
        {"name" : "Cold Coffee", "price": 80},
    ]
     
     return render (request,'home/menu.html',{"menu_items" : menu_items})
