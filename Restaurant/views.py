
from django.shortcuts import render
from rest_framework import generics
from .serializers import menuSerializer,bookingSerializer
from rest_framework.decorators import api_view
from .models import Menu

def index(request):
 return render(request, 'index.html', {"":""})

# def post(self,request):
#   serializer = menuSerializer(data=request.data)

#   if serializer.is_valid():
#     serializer.save()

#     return Response({"status":"success","data":serializer.data})
  


# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
 queryset = Menu.objects.all()
 serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = menuSerializer