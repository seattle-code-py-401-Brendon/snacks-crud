from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy


class Homepageview(TemplateView):
    template_name = 'home.html'


class SnackListView(ListView):
    template_name = 'snack-list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack-detail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'snack-create.html'
    model = Snack
    fields = ['title', 'description', 'purchaser']


class SnackUpdateView(UpdateView):
    template_name = 'snack-update.html'
    model = Snack
    fields = ['title', 'description', 'purchaser']


class SnackDeleteView(DeleteView):
    template_name = 'snack-delete.html'
    model = Snack
    fields = ['title', 'description', 'purchaser']

