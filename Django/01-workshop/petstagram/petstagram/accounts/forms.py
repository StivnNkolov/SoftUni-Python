from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from petstagram.accounts.models import Profile
from petstagram.common.helpers import BootstrapFormMixin
from django.contrib.auth.forms import AuthenticationForm

from petstagram.main_app.models import PetPhoto


class CreateProfileForm(BootstrapFormMixin, UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_MAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    profile_picture = forms.URLField(

    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password2'].label = 'Confirm Password'
        self.fields['profile_picture'].label = 'Link to Profile Picture'

        self.fields['username'].widget = forms.TextInput(
            attrs={
                'placeholder': 'Enter username',
            },
        )
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password',
            }
        )
        self.fields['password2'].widget = forms.PasswordInput(

            attrs={
                'placeholder': 'Enter password again',
            },
        )
        self.fields['first_name'].widget = forms.TextInput(
            attrs={
                'placeholder': 'Enter first name',
            },
        )
        self.fields['last_name'].widget = forms.TextInput(
            attrs={
                'placeholder': 'Enter last name',
            },
        )
        self.fields['profile_picture'].widget = forms.URLInput(
            attrs={
                'placeholder': 'Enter URL',
            },
        )

        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            profile_picture=self.cleaned_data['profile_picture'],
        )
        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'profile_picture']
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter first name',
        #             # 'class': 'form-control',
        #         },
        #     ),
        #     'last_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter last name',
        #             # 'class': 'form-control',
        #         },
        #     ),
        #     'profile_picture': forms.URLInput(
        #         attrs={
        #             'placeholder': 'Enter URL',
        #             # 'class': 'form-control',
        #         }
        #     )
        # }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW_GENDER

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture', 'date_of_birth', 'email', 'gender', 'description')
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


class LogInForm(BootstrapFormMixin, AuthenticationForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(
            attrs={
                'placeholder': 'Enter username',
            },
        )
        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password',
            },
        )

        self._init_bootstrap_form_controls()


# TODO coupled to make sure that when the picture is delete we delete in our machine Stivi you crazy biatch
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


class ChangePasswordForm(BootstrapFormMixin, PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Enter current password',
            },
        )

        self.fields['new_password1'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Enter new password',
            },
        )

        self.fields['new_password2'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm new password',
            },
        )

        self._init_bootstrap_form_controls()
