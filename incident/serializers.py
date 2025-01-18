from rest_framework import serializers
from .models import Incident


class IncidentViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Incident
        exclude = ['id']


class IncidentSerialiZers(serializers.ModelSerializer):
    class Meta:
        model = Incident
        exclude = ['incident_id', 'user_id', 'id']