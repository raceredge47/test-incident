from .serializers import IncidentSerialiZers, IncidentViewSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import views, response, status
from datetime import datetime
from .models import Incident
import random
# Create your views here.


class IncidentAPIView(views.APIView):
    serializer_class = IncidentViewSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request):
        incidents = Incident.objects.filter(
            user_id=request.user
        )
        return response.Response({
            'incidents': self.serializer_class(incidents, many=True).data,
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = IncidentSerialiZers(data=request.data)
        if serializer.is_valid():
            incident = Incident.objects.create(
                **serializer.validated_data,                
                user_id=request.user,
                incident_id=f'RMG{random.randint(10000, 99999)}{datetime.now().year}'
                )
            return response.Response(self.serializer_class(incident).data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            incident = Incident.objects.get(incident_id=pk)
            if incident.status == Incident.CLOSED:
                return response.Response({
                    'error': 'You can not update closed incident.'
                }, status=status.HTTP_400_BAD_REQUEST)
        except Incident.DoesNotExist:
            return response.Response({
                'error': 'Incident not found.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = IncidentSerialiZers(incident, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(self.serializer_class(incident).data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)