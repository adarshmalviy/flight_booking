from django.urls import path
from . import views
from users.views import dashboard_view
app_name = 'flights'

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('search/', views.search_flights, name='search_flights'),
    path('book_flight/', views.book_flight, name='book_flight'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
]
