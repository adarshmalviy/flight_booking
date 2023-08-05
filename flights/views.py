
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'flights/view_bookings.html', {'bookings': bookings})

@api_view(['POST', 'GET'])
def search_flights(request):
    if request.method == 'POST':
        source_city = request.POST.get('source_city')
        destination_city = request.POST.get('destination_city')
        date = request.POST.get('date')
        time = request.POST.get('time')
        flight_number = request.POST.get('flight_number')
        flight_id = request.POST.get('flight_id')

        flights = Flight.objects.all()

        if source_city:
            flights = flights.filter(source_city=source_city)

        if destination_city:
            flights = flights.filter(destination_city=destination_city)

        if date:
            flights = flights.filter(departure_time__date=date)

        if time:
            flights = flights.filter(departure_time__time=time)

        if flight_number:
            flights = flights.filter(flight_number=flight_number)

        if flight_id:
            flights = flights.filter(id=flight_id)

        serializer = FlightSerializer(flights, many=True)
        return render(request, 'flights/search_flights.html', {'flights': serializer.data})

    elif request.method == 'GET':
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return render(request, 'flights/search_flights.html', {'flights': serializer.data})

    return Response({'message': 'Please make a POST or GET request with appropriate parameters.'}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
@login_required
def book_flight(request):
    if request.method == 'POST':
        flight_number = request.POST.get('flight_number')
        try:
            flight = Flight.objects.get(flight_number=flight_number)

        except Flight.DoesNotExist:
            return render(request, 'flights/booking_failed.html', {'error_message': f'Flight with number {flight_number} not found.'})

        if request.method == 'POST':
            user = request.user
        
        # Check if the user has already booked this flight
        if Booking.objects.filter(user=user, flight=flight).exists():
            return render(request, 'flights/booking_failed.html', {'error_message': f'You have already booked this flight.'})

        # Check if flight is available for booking
        if flight.seat_count > 0:
            booking = Booking(user=request.user, flight=flight)
            booking.save()

            # Reduce seat_count by 1 after successful booking
            flight.seat_count -= 1
            flight.save()

            return render(request, 'flights/book_flight.html', {'message': f'Booking successful for flight {flight.flight_number}. Seat booked.'})

        else:
            return render(request, 'flights/booking_failed.html', {'error_message': f'Booking failed. No seats available for flight {flight.flight_number}.'})

    return render(request, 'flights/book_flight.html')
