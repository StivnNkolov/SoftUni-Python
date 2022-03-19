from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from petstagram.main_app.views.generic import home, dashboard, denied_access
from petstagram.main_app.views.pets import create_pet, edit_pet, delete_pet
from petstagram.main_app.views.photos import photo_details, add_like, create_pet_photo, edit_pet_photo, delete_photo
from petstagram.main_app.views.profile import profile_description, create_profile, edit_profile, delete_profile

urlpatterns = [
    path('', home, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile_description, name='profile'),
    path('photo/detail/<int:pk>/', photo_details, name='photo details'),
    path('photo/like/<int:pk>/', add_like, name='like pet'),
    path('denied/', denied_access, name='401'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('pet/add/', create_pet, name='add pet'),
    path('pet/edit/<int:pk>/', edit_pet, name='edit pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='delete pet'),

    path('photo/add/', create_pet_photo, name='add photo'),
    path('photo/edit/<int:pk>', edit_pet_photo, name='edit photo'),
    path('photo/delete/<int:pk>', delete_photo, name='delete photo'),

]
