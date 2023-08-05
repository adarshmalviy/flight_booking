from django.urls import path
from . import views

urlpatterns = [
     path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('add_flight/', views.AddFlightView.as_view(), name='add_flight'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('remove_flight/', views.remove_flight, name='remove_flight'),

    # View All Bookings
    path('view_all_bookings/', views.view_all_bookings, name='view_all_bookings'),

]

