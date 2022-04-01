# TODO use your disabled mixin instead of doing it on hand punk. Add some more mixins you need em!@@@
from django.shortcuts import redirect
from django.urls import reverse_lazy


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            # if self.__class__.__name__ == 'DeletePetForm':
            #     # field.widget.attrs['required'] = False
            #     field.widget.attrs['readonly'] = True
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget)
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'
            if field.widget.__class__.__name__ == 'FileInput':
                field.widget.attrs['class'] = 'form-control-file'


class DisabledFormMixin:
    disabled_fields = '__all__'
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            if self.disabled_fields != '__all__' and name not in self.disabled_fields:
                continue
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


class AuthenticationRedirectToLoginMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('log in')
        return super().dispatch(request, *args, **kwargs)


class AuthenticationRedirectToDashboardMixin:

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class GetSuccessUrlToProfileDetails:

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.id})
