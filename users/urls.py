from django.urls import path, include
from .views import UserSignupView, user_login, user_logout,dashboard_view

# app_name = 'users'

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user_signup'),
    path('login/', user_login, name='user_login'),
    path('api-auth/', include('rest_framework.urls')),
    path('logout/', user_logout, name='user_logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
]


