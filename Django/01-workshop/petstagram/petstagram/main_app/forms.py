from django import forms

from petstagram.main_app.helpers import BootstrapFormMixin, DisabledFormMixin, find_profile, find_pets_for_profile
from petstagram.main_app.models import Profile, Pet, PetPhoto


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                    # 'class': 'form-control',
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                    # 'class': 'form-control',
                },
            ),
            'profile_picture': forms.URLInput(
                attrs={
                    'placeholder': 'Enter URL',
                    # 'class': 'form-control',
                }
            )
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW_GENDER

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                },
            ),
            'profile_picture': forms.URLInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'min': '1920-01-01',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),

            'gender': forms.Select(
                choices=Profile.GENDERS,
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Enter description'
                }
            )
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        photos = PetPhoto.objects.filter(tagged_pets__in=pets)
        photos.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = []


class PetForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = ['name', 'type', 'date_of_birth']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                },
            ),

        }


class DeletePetForm(BootstrapFormMixin, DisabledFormMixin, forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    class Meta:
        model = Pet
        fields = ['name', 'type', 'date_of_birth']


class CreatePhotoForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto
        fields = ['photo', 'description', 'tagged_pets']
        widgets = {
            'photo': forms.FileInput(
                attrs={
                    # 'class': 'form-control-file',
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Enter description',
                },
            ),
            'tagged_pets': forms.SelectMultiple(

            )
        }


class EditPhotoForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto
        fields = ['description', 'tagged_pets']
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                },
            ),
        }
