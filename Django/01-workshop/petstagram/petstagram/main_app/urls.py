from django.urls import path

from petstagram.main_app.views.generic import HomeView, DashboardView
from petstagram.main_app.views.pets import CreatePet, EditPet, DeletePet
from petstagram.main_app.views.photos import add_like, CreatePhotoView, delete_photo, \
    PhotoDetailsView, EditPhotoView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('photo/detail/<int:pk>/', PhotoDetailsView.as_view(), name='photo details'),
    path('photo/like/<int:pk>/', add_like, name='like pet'),
    # path('denied/', denied_access, name='401'),

    path('pet/add/', CreatePet.as_view(), name='add pet'),
    path('pet/edit/<int:pk>/', EditPet.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', DeletePet.as_view(), name='delete pet'),

    path('photo/add/', CreatePhotoView.as_view(), name='add photo'),
    path('photo/edit/<int:pk>', EditPhotoView.as_view(), name='edit photo'),
    path('photo/delete/<int:pk>', delete_photo, name='delete photo'),

]
