from django.contrib.auth import login, logout, authenticate
from rest_framework.decorators import api_view, permission_classes, authentication_classes,renderer_classes
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer, UserLoginSerializer
from django.shortcuts import render, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponse

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return HttpResponse('Invalid credentials. Please try again.', status=401)

        if user.check_password(password):
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with the name of your dashboard view or URL name
        else:
            return HttpResponse('Invalid credentials. Please try again.', status=401)

    return render(request, 'users/login.html')

@login_required
def dashboard_view(request):
    # Logic for displaying the dashboard page
    print("dashboard loading..")
    return render(request, 'users/dashboard.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')  # Redirect to the user login page


class UserSignupView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)



# def user_login(request):
#     if request.method == 'POST':
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         username = serializer.validated_data.get('username')
#         password = serializer.validated_data.get('password')
#         user = CustomUser.objects.get(username=username)
#         if user.check_password(password):
#             login(request, user)
#             return redirect('user_dashboard')  # Redirect to the user dashboard page
#         else:
#             message = "Invalid credentials. Please try again."
#             return render(request, 'users/login.html', {'message': message})
#     return render(request, 'users/login.html')


# @api_view(['POST'])
# @permission_classes([AllowAny])
# @authentication_classes([])
# def user_login(request):
#     serializer = UserLoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     username = serializer.validated_data.get('username')
#     password = serializer.validated_data.get('password')
#     print(username, password)
#     try:
#         user = CustomUser.objects.get(username=username)
#     except CustomUser.DoesNotExist:
#         return Response({'message': 'Invalid Username. Please try again.'}, status=status.HTTP_401_UNAUTHORIZED)

#     if user.check_password(password):
#         login(request, user)
#         return Response({'message': 'User login successful.'})

#     return render(request, 'users/login.html', {'message': 'Invalid credentials. Please try again.'})
#     # return Response({'message': 'Invalid credentials. Please try again.'}, status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['POST'])
# def user_logout(request):
#     logout(request)
#     return Response({'message': 'User logout successful.'})


    # user = authenticate(request, username=username, password=password)
    # print(user)
    # if user is not None:
    #     login(request, user)
    #     return Response({'message': 'User login successful.'})
    # return Response({'message': 'Invalid credentials. Please try again.'}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# @authentication_classes([])
# def user_login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     print(username)
#     print("---")
#     print(password)
#     print("--")
#     user = authenticate(request, username=username, password=password)
#     print(user)
#     if user is not None:
#         login(request, user)
#         return Response({'message': 'User login successful.'})
#     return Response({'message': 'Invalid credentials. Please try again.'}, status=status.HTTP_401_UNAUTHORIZED)

