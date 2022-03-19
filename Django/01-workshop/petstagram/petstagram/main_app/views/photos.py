from django.shortcuts import redirect, render

from petstagram.main_app.forms import CreatePhotoForm, EditPhotoForm
from petstagram.main_app.models import PetPhoto
from petstagram.main_app.helpers import find_profile


def crud_operations_photo(request, form_instance, redirect_to, model_instance, render_page):
    if find_profile() is None:
        return redirect('401')
    form = form_instance(instance=model_instance)

    if request.method == 'POST':
        form = form_instance(request.POST, request.FILES, instance=model_instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_to)

    context = {
        'form': form,
        'photo': model_instance,
    }
    return render(request, render_page, context)


def photo_details(request, pk):
    current_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(id=pk)

    if find_profile() is None:
        return redirect('401')

    context = {

        'current_photo': current_photo,
    }

    return render(request, 'photo_details.html', context)


def create_pet_photo(request):
    # form = CreatePhotoForm()
    #
    # if request.method == 'POST':
    #     form = CreatePhotoForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('dashboard')
    #
    # context = {
    #     'form': form,
    # }
    #
    # return render(request, 'photo_create.html', context)
    # form = CreatePhotoForm()
    #
    # if request.method == 'POST':
    #     form = CreatePhotoForm(request.POST)
    #     if form.is_valid():
    #         photo = PetPhoto(
    #             photo=form.cleaned_data['photo'],
    #             description=form.cleaned_data[''],
    #             tagged_pets=form.cleaned_data['tagged_pets'],
    #         )
    #         photo.save()
    #         return redirect('dashboard')
    #
    # context = {
    #     'form': form,
    # }
    # return render(request, 'photo_create.html', context)

    return crud_operations_photo(request, CreatePhotoForm, 'dashboard', PetPhoto(), 'photo_create.html')


def edit_pet_photo(request, pk):
    photo = PetPhoto.objects.get(id=pk)
    form = EditPhotoForm(instance=photo)

    if request.method == 'POST':
        form = EditPhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo details', pk)

    context = {
        'form': form,
        'photo': photo,

    }

    return render(request, 'photo_edit.html', context)


def delete_photo(request, pk):
    current_photo = PetPhoto.objects.get(id=pk)
    current_photo.delete()
    return redirect('dashboard')


def add_like(request, pk):
    current_photo = PetPhoto.objects.get(id=pk)
    current_photo.likes += 1
    current_photo.save()
    return redirect('photo details', pk)
