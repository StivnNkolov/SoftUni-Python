from django import forms
from petstagram.common.helpers import BootstrapFormMixin, DisabledFormMixin
from petstagram.main_app.models import Pet, PetPhoto


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.user = self.user
        if commit:
            pet.save()
        return pet

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


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = '__all__'


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

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        smt = super().save(commit=False)
        smt.user = self.user
        if commit:
            smt.save()
        return smt

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
