from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from django.shortcuts import render
from .serializer import FlightSerializer, BookingSerializer
from datetime import *

class Flights(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer	

class Bookings(ListAPIView):
	queryset = Booking.objects.filter(date__gt = date.today())
	serializer_class = BookingSerializer	
		