from django.urls import path
from user import views

# used for url reverse function , app_name:action_name , eg: user:create
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateAuthTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
