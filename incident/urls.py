from .views import IncidentAPIView
from django.urls import path


urlpatterns = [
    path('', IncidentAPIView.as_view(), name='incident'),
    path('<str:pk>/', IncidentAPIView.as_view(), name='incident_update')
]
