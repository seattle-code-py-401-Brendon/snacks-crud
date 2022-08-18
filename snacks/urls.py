from django.urls import path
from .views import Homepageview, SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('', Homepageview.as_view(), name='home'),
    path('snack_list/', SnackListView.as_view(), name='list_snacks'),
    path('<int:pk>/', SnackDetailView.as_view(), name='detail_snack'),
]
