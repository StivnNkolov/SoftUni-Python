from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from petstagram.main_app.forms import CreatePetForm, DeletePetForm, EditPetForm
from petstagram.main_app.models import Pet


class CreatePet(CreateView):
    template_name = 'main_app/pet_create.html'
    success_url = reverse_lazy('dashboard')
    form_class = CreatePetForm
    model = Pet

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('log in')
        return super().dispatch(request, *args, **kwargs)


class EditPet(UpdateView):
    template_name = 'main_app/pet_edit.html'
    model = Pet
    # fields = '__all__'
    form_class = EditPetForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.id})


class DeletePet(UpdateView):
    template_name = 'main_app/pet_delete.html'
    model = Pet
    form_class = DeletePetForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.id})

# def delete_pet(request, pk):
#     # pet = Pet.objects.get(id=pk)
#     # form = DeletePetForm(instance=pet)
#     #
#     # if request.method == 'POST':
#     #     # form = DeletePetForm(request.POST, instance=pet)
#     #     pet.delete()
#     #     return redirect('profile')
#     #
#     # context = {
#     #     'form': form,
#     # }
#     #
#     # return render(request, 'pet_delete.html', context)
#     return crud_operations_pet(request, DeletePetForm, 'profile', Pet.objects.get(id=pk), 'main_app/pet_delete.html')
#
# def crud_operations_pet(request, form_instance, redirect_to, model_instance, render_page):
#     # if find_profile() is None:
#     #     return redirect('401')
#     form = form_instance(instance=model_instance)
#
#     if request.method == 'POST':
#         form = form_instance(request.POST, request.FILES, instance=model_instance)
#         if form.is_valid():
#             form.save()
#             return redirect(redirect_to)
#
#     context = {
#         'form': form,
#         'pet': model_instance,
#     }
#     return render(request, render_page, context)
#
#
# def edit_pet(request, pk):
#     # pet = Pet.objects.get(id=pk)
#     # form = CreateUpdatePetForm(instance=pet)
#     #
#     # if request.method == 'POST':
#     #     form = CreateUpdatePetForm(request.POST, instance=pet)
#     #     if form.is_valid():
#     #         form.save()
#     #     return redirect('profile')
#     #
#     # context = {
#     #     'form': form,
#     # }
#     # return render(request, 'pet_edit.html', context)
#     return crud_operations_pet(request, CreatePetForm, 'profile', Pet.objects.get(id=pk), 'pet_edit.html')
#
# def create_pet(request):
#     # form = CreatePetForm()
#     # current_profile = find_profile()
#     # if request.method == 'POST':
#     #     form = CreatePetForm(request.POST, instance=Pet(user_profile=current_profile))
#     #
#     #     if form.is_valid():
#     #         form.save()
#     #     return redirect('profile')
#     #
#     # context = {
#     #     'form': form,
#     # }
#     # return render(request, 'pet_create.html', context)
#     return crud_operations_pet(request, CreatePetForm, 'profile', Pet(user_profile=find_profile()),
#                                'main_app/pet_create.html')
