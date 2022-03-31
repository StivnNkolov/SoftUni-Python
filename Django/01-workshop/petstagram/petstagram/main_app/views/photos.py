from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, DetailView, UpdateView

from petstagram.main_app.forms import CreatePhotoForm, EditPhotoForm
from petstagram.main_app.models import PetPhoto


class CreatePhotoView(CreateView):
    template_name = 'main_app/photo_create.html'
    form_class = CreatePhotoForm
    success_url = reverse_lazy('dashboard')
    model = PetPhoto

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('log in')
        return super().dispatch(request, *args, **kwargs)


class PhotoDetailsView(DetailView):
    template_name = 'main_app/photo_details.html'
    model = PetPhoto
    context_object_name = 'current_photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class EditPhotoView(UpdateView):
    template_name = 'main_app/photo_edit.html'
    model = PetPhoto
    form_class = EditPhotoForm
    success_url = reverse_lazy('photo details')

    def get_success_url(self):
        return reverse_lazy('photo details', kwargs={'pk': self.object.id})


def delete_photo(request, pk):
    current_photo = PetPhoto.objects.get(id=pk)
    current_photo.delete()
    return redirect('dashboard')


def add_like(request, pk):
    current_photo = PetPhoto.objects.get(id=pk)
    current_photo.likes += 1
    current_photo.save()
    return redirect('photo details', pk)

# def edit_pet_photo(request, pk):
#     photo = PetPhoto.objects.get(id=pk)
#     form = EditPhotoForm(instance=photo)
#
#     if request.method == 'POST':
#         form = EditPhotoForm(request.POST, instance=photo)
#         if form.is_valid():
#             form.save()
#             return redirect('photo details', pk)
#
#     context = {
#         'form': form,
#         'photo': photo,
#
#     }
#
#     return render(request, 'main_app/photo_edit.html', context)
#
#
#
# def photo_details(request, pk):
#     current_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(id=pk)
#
#     if find_profile() is None:
#         return redirect('401')
#
#     context = {
#
#         'current_photo': current_photo,
#     }
#
#     return render(request, 'main_app/photo_details.html', context)
#
#
# def create_pet_photo(request):
#     # form = CreatePhotoForm()
#     #
#     # if request.method == 'POST':
#     #     form = CreatePhotoForm(request.POST, request.FILES)
#     #     if form.is_valid():
#     #         form.save()
#     #     return redirect('dashboard')
#     #
#     # context = {
#     #     'form': form,
#     # }
#     #
#     # return render(request, 'photo_create.html', context)
#     # form = CreatePhotoForm()
#     #
#     # if request.method == 'POST':
#     #     form = CreatePhotoForm(request.POST)
#     #     if form.is_valid():
#     #         photo = PetPhoto(
#     #             photo=form.cleaned_data['photo'],
#     #             description=form.cleaned_data[''],
#     #             tagged_pets=form.cleaned_data['tagged_pets'],
#     #         )
#     #         photo.save()
#     #         return redirect('dashboard')
#     #
#     # context = {
#     #     'form': form,
#     # }
#     # return render(request, 'photo_create.html', context)
#
#     return crud_operations_photo(request, CreatePhotoForm, 'dashboard', PetPhoto(), 'photo_create.html')
