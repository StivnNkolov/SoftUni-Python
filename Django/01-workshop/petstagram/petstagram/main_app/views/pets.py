from django.shortcuts import render, redirect

from petstagram.main_app.forms import PetForm, DeletePetForm
from petstagram.main_app.helpers import find_profile
from petstagram.main_app.models import Pet


def crud_operations_pet(request, form_instance, redirect_to, model_instance, render_page):
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
        'pet': model_instance,
    }
    return render(request, render_page, context)


def create_pet(request):
    # form = CreatePetForm()
    # current_profile = find_profile()
    # if request.method == 'POST':
    #     form = CreatePetForm(request.POST, instance=Pet(user_profile=current_profile))
    #
    #     if form.is_valid():
    #         form.save()
    #     return redirect('profile')
    #
    # context = {
    #     'form': form,
    # }
    # return render(request, 'pet_create.html', context)
    return crud_operations_pet(request, PetForm, 'profile', Pet(user_profile=find_profile()), 'pet_create.html')


def edit_pet(request, pk):
    # pet = Pet.objects.get(id=pk)
    # form = CreateUpdatePetForm(instance=pet)
    #
    # if request.method == 'POST':
    #     form = CreateUpdatePetForm(request.POST, instance=pet)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('profile')
    #
    # context = {
    #     'form': form,
    # }
    # return render(request, 'pet_edit.html', context)
    return crud_operations_pet(request, PetForm, 'profile', Pet.objects.get(id=pk), 'pet_edit.html')


def delete_pet(request, pk):
    # pet = Pet.objects.get(id=pk)
    # form = DeletePetForm(instance=pet)
    #
    # if request.method == 'POST':
    #     # form = DeletePetForm(request.POST, instance=pet)
    #     pet.delete()
    #     return redirect('profile')
    #
    # context = {
    #     'form': form,
    # }
    #
    # return render(request, 'pet_delete.html', context)
    return crud_operations_pet(request, DeletePetForm, 'profile', Pet.objects.get(id=pk), 'pet_delete.html')
