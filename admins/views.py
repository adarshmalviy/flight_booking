
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

