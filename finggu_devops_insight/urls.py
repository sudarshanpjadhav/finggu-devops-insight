from django.urls import path
from .views import FingguDashboardView

urlpatterns = [
    path('', FingguDashboardView.as_view(), name='dashboard'),
]