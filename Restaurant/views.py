
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import menuSerializer,bookingSerializer,UserSerializer
from rest_framework.decorators import api_view
from .models import Menu,Booking
from django.contrib.auth.models import User
from rest_framework import permissions

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


class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = bookingSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 