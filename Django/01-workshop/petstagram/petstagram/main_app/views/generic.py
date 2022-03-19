from django.shortcuts import render, redirect

from petstagram.main_app.models import PetPhoto
from petstagram.main_app.helpers import find_profile


def home(request):
    hide_additional_items = True
    context = {
        'hide_items': hide_additional_items,
    }

    return render(request, 'home_page.html', context)


def dashboard(request):
    current_profile = find_profile()

    if current_profile is None:
        return redirect('401')
    pet_photos = set(PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=current_profile))

    context = {
        'pet_photos': pet_photos,
    }

    return render(request, 'dashboard.html', context)


def denied_access(request):
    return render(request, 'tags/401_error.html')
