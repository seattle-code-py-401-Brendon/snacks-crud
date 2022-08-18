from django.urls import path
from .views import Homepageview, SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('', Homepageview.as_view(), name='home'),
    path('snack_list/', SnackListView.as_view(), name='list_snacks'),
    path('<int:pk>/', SnackDetailView.as_view(), name='detail_snack'),
    path('create/', SnackCreateView.as_view(), name='create_snack'),
    path('update/<int:pk>/', SnackUpdateView.as_view(), name='update_snack'),
    path('delete/<int:pk>', SnackDeleteView.as_view(), name='delete_snack'),
]
