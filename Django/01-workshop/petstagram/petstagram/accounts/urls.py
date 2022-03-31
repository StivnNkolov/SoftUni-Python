from django.contrib.auth.views import LogoutView
from django.urls import path

from petstagram.accounts.views import UserLoginView, UserRegisterView, UserProfileDetailsView, EditProfileView, \
    DeleteProfileView, ChangeUserPasswordView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileDetailsView.as_view(), name='profile details'),

    path('log-in/', UserLoginView.as_view(), name='log in'),
    path('edit-profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('edit-password/<int:pk>/', ChangeUserPasswordView.as_view(), name='edit password'),
    path('delete-profile/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
