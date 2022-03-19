from django.shortcuts import redirect, render

from petstagram.main_app.models import Profile, Pet


def find_profile():
    first_profile = Profile.objects.all()

    if first_profile:
        return first_profile[0]
    else:
        return None


def find_pets_for_profile():
    profile = find_profile()
    if not profile:
        return None
    pets = profile.pet_set.all()
    if pets:
        return pets
    return None


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
            field.widget.attrs['readonly'] = True

# def crud_operations(request, form_instance, redirect_to, model_instance, render_page):
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
