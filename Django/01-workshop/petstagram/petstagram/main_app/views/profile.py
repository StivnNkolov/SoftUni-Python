from django.shortcuts import redirect, render

from petstagram.main_app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.main_app.models import Pet, PetPhoto, Profile
from petstagram.main_app.helpers import find_profile


def crud_operations_profile(request, form_instance, redirect_to, model_instance, render_page):
    if find_profile() is None and form_instance.__name__ != 'CreateProfileForm':
        return redirect('401')
    form = form_instance(instance=model_instance)

    if request.method == 'POST':
        form = form_instance(request.POST, request.FILES, instance=model_instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_to)

    context = {
        'form': form,
    }
    return render(request, render_page, context)


def profile_description(request):
    current_profile = find_profile()

    if current_profile is None:
        return redirect('401')

    users_pets = list(Pet.objects.filter(user_profile=current_profile))
    photos = PetPhoto.objects.filter(tagged_pets__in=users_pets).distinct()
    total_images = len(photos)
    total_likes = sum([el.likes for el in photos])

    context = {
        'current_profile': current_profile,
        'total_images': total_images,
        'total_likes': total_likes,
        'users_pets': users_pets,
    }

    return render(request, 'profile_details.html', context)


def create_profile(request):
    # form = CreateProfileForm()
    #
    # if request.method == 'POST':
    #     form = CreateProfileForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('index')
    # context = {
    #     'form': form,
    # }
    # return render(request, 'profile_create.html', context)
    return crud_operations_profile(request, CreateProfileForm, 'index', Profile(), 'profile_create.html')


def edit_profile(request):
    # current_profile = find_profile()
    # form = EditProfileForm(instance=current_profile)
    #
    # if request.method == 'POST':
    #     form = EditProfileForm(request.POST, instance=current_profile)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('profile')
    #
    # context = {
    #     'form': form,
    # }
    # return render(request, 'profile_edit.html', context)
    return crud_operations_profile(request, EditProfileForm, 'profile', find_profile(), 'profile_edit.html')


def delete_profile(request):
    return crud_operations_profile(request, DeleteProfileForm, 'profile', find_profile(), 'profile_delete.html')
