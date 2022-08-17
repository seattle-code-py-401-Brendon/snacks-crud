from django.urls import path
from .views import Homepageview, SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('', Homepageview.as_view(), name='home'),
]