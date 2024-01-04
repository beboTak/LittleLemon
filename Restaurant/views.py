
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import menuSerializer,bookingSerializer,UserSerializer
from .models import Menu,Booking
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import  HttpResponse

def index(request):
 return render(request, 'index.html', {"":""})

# def post(self,request):
#   serializer = menuSerializer(data=request.data)

#   if serializer.is_valid():
#     serializer.save()

#     return Response({"status":"success","data":serializer.data})
  


# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
 permission_classes = [IsAuthenticated] 
 queryset = Menu.objects.all()
 serializer_class = menuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = menuSerializer


class BookingViewSet(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated]
   queryset = Booking.objects.all()
   serializer_class = bookingSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 





@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
  return  HttpResponse({"message":"This view is protected"})