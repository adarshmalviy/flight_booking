
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from flights.models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from flights.models import Flight
from flights.forms import FlightForm


@login_required(login_url='/admins/login/')
def admin_dashboard(request):
    flights = Flight.objects.all()
    return render(request, 'admins/dashboard.html', {'flights': flights})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'admins/login.html', {'error_message': 'Invalid credentials. Please try again.'})

    return render(request, 'admins/login.html')

@login_required(login_url='/admins/login/')
def admin_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('admin_login')

    return render(request, 'admins/logout.html')



# class AddFlightView(CreateView):
#     model = Flight
#     form_class = FlightForm
#     template_name = 'admins/add_flight.html'
#     success_url = '/admins/dashboard/'

# @login_required(login_url='/admins/login/')
class AddFlightView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Flight
    form_class = FlightForm
    template_name = 'admins/add_flight.html'
    success_url = reverse_lazy('admin_dashboard')
    login_url = '/admins/login/'

    def test_func(self):
        return self.request.user.is_superuser

@login_required(login_url='/admins/login/')
def remove_flight(request):
    if request.method == 'POST':
        flight_id = request.POST.get('flight_id')
        try:
            flight = Flight.objects.get(pk=flight_id)
            flight.delete()
            return redirect('admin_dashboard')
        except Flight.DoesNotExist:
            return render(request, 'admins/remove_flight.html', {'error_message': 'Flight not found.'})

    return render(request, 'admins/remove_flight.html')

@login_required(login_url='/admins/login/')
def view_all_bookings(request):
    if request.method == 'POST':
        flight_number = request.POST.get('flight_number')
        try:
            flight = Flight.objects.get(flight_number=flight_number)
            bookings = Booking.objects.filter(flight=flight)
            return render(request, 'admins/view_all_bookings.html', {'bookings': bookings, 'flight_number': flight_number})
        except Flight.DoesNotExist:
            return render(request, 'admins/view_all_bookings.html', {'error_message': 'Flight not found.'})

    return render(request, 'admins/view_all_bookings.html')

# class RemoveFlightView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Flight
#     template_name = 'admins/remove_flight.html'
#     success_url = reverse_lazy('admin_dashboard')
#     login_url = '/users/login/'

#     def test_func(self):
#         return self.request.user.is_superuser

# class ViewAllBookingsView(LoginRequiredMixin, UserPassesTestMixin, ListView):
#     model = Booking
#     serializer_class = BookingSerializer
#     template_name = 'admins/view_all_bookings.html'
#     login_url = '/users/login/'

#     def get_queryset(self):
#         flight_number = self.kwargs['flight_number']
#         return Booking.objects.filter(flight__flight_number=flight_number)

#     def test_func(self):
#         return self.request.user.is_superuser



# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def add_flight(request):
#     serializer = FlightSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# @permission_classes([IsAdminUser])
# def remove_flight(request, flight_id):
#     try:
#         flight = Flight.objects.get(pk=flight_id)
#     except Flight.DoesNotExist:
#         return Response({'message': 'Flight not found.'}, status=status.HTTP_404_NOT_FOUND)

#     flight.delete()
#     return Response({'message': 'Flight removed successfully.'}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @permission_classes([IsAdminUser])
# def view_all_bookings(request, flight_number):
#     # , flight__departure_time=departure_time
#     try:
#         bookings = Booking.objects.filter(flight__flight_number=flight_number)
#     except Booking.DoesNotExist:
#         return Response({'message': 'No bookings found for the flight.'}, status=status.HTTP_404_NOT_FOUND)

#     serializer = BookingSerializer(bookings, many=True)
#     return Response({'bookings': serializer.data}, status=status.HTTP_200_OK)



# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, authenticate, logout
# from django.shortcuts import render, redirect
# from flights.models import Flight, Booking

# @login_required
# def add_flight(request):
#     if request.method == 'POST':
#         flight_number = request.POST['flight_number']
#         date = request.POST['date']
#         time = request.POST['time']
#         availability = request.POST['availability']
#         flight = Flight(flight_number=flight_number, date=date, time=time, availability=availability)
#         flight.save()
#         return redirect('view_all_flights')
#     return render(request, 'admins/add_flight.html')

# @login_required
# def remove_flight(request, flight_id):
#     flight = Flight.objects.get(pk=flight_id)
#     flight.delete()
#     return redirect('view_all_flights')

# @login_required
# def view_all_flights(request):
#     flights = Flight.objects.all()
#     return render(request, 'admins/view_all_flights.html', {'flights': flights})

# @login_required
# def view_all_bookings(request):
#     if request.method == 'POST':
#         flight_number = request.POST['flight_number']
#         flight = Flight.objects.get(flight_number=flight_number)
#         bookings = Booking.objects.filter(flight=flight)
#         return render(request, 'admins/view_all_bookings.html', {'bookings': bookings})
#     return render(request, 'admins/view_all_bookings.html')


# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None and user.is_staff:
#             login(request, user)
#             return redirect('view_all_flights')  # Redirect to a dashboard page for admin
#         else:
#             message = "Invalid admin credentials. Please try again."
#             return render(request, 'admins/login.html', {'message': message})
#     return render(request, 'admins/login.html')

# def admin_logout(request):
#     logout(request)
#     return redirect('admin_login')