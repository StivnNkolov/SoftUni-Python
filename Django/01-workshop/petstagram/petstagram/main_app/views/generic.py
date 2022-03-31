from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from petstagram.main_app.models import PetPhoto


#
# def home(request):
#     hide_additional_items = True
#     context = {
#         'hide_items': hide_additional_items,
#     }
#
#     return render(request, 'main_app/home_page.html', context)
#
#
# def dashboard(request):
#     pet_photos = PetPhoto.objects.all()
#
#     context = {
#         'pet_photos': pet_photos,
#     }
#
#     return render(request, 'main_app/dashboard.html', context)

class HomeView(TemplateView):
    template_name = 'main_app/home_page.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class DashboardView(ListView):
    template_name = 'main_app/dashboard.html'
    model = PetPhoto
    context_object_name = 'pet_photos'


# def denied_access(request):
#     return render(request, 'tags/401_error.html')
