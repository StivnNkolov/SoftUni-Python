from django.contrib.auth.views import LoginView, PasswordChangeView

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, LogInForm, \
    ChangePasswordForm
from petstagram.accounts.models import Profile
from django.contrib.auth import logout

from petstagram.main_app.models import Pet, PetPhoto


class UserLoginView(LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')
    form_class = LogInForm

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class UserRegisterView(CreateView):
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('index')
    form_class = CreateProfileForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class ChangeUserPasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('log in')
    form_class = ChangePasswordForm

    def form_valid(self, form):
        logout(self.request)
        return super().form_valid(form)


class UserProfileDetailsView(DetailView):
    template_name = 'accounts/profile_details.html'
    model = Profile
    context_object_name = 'current_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = Pet.objects.filter(user=self.request.user).all()
        all_images = PetPhoto.objects.filter(user=self.request.user)
        images_count = all_images.count()
        total_likes = sum([el.likes for el in all_images])

        context['user_pets'] = pets
        context['total_images'] = images_count
        context['total_likes'] = total_likes

        return context


class EditProfileView(UpdateView):
    template_name = 'accounts/profile_edit.html'
    model = Profile
    form_class = EditProfileForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.id})


class DeleteProfileView(DeleteView):
    template_name = 'accounts/profile_delete.html'
    model = Profile
    success_url = reverse_lazy('index')
    form_class = DeleteProfileForm

    def form_valid(self, form):
        profile = self.object
        user = profile.user
        logout(self.request)
        profile.delete()
        user.delete()
        return redirect(self.success_url)
