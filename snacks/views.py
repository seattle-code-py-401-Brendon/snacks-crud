from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack

class Homepageview(TemplateView):
    template_name = 'home.html'

class SnackListView(ListView):
    template_name = 'snack-list.html'
    model = Snack

class SnackDetailView(DeleteView):
    template_name = 'snack-detail.html'

class SnackCreateView(CreateView):
    template_name = 'snack-create.html'

class SnackUpdateView(UpdateView):
    template_name = 'snack-update.html'

class SnackDeleteView(DeleteView):
    template_name = 'snack-delete.html'
