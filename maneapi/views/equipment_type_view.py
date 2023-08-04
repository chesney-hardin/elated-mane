"""View module for handling requests about equipmentTypes"""
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from maneapi.models import Equipment, EquipmentType


class EquipmentTypeView(ViewSet):
    """Viewset for equipmentTypes"""

    def update(self, request, pk=None):
        """Handle PUT requests for a equipmentType

        Returns:
            Response -- Empty body with 204 status code
        """
        label = request.data.get("label", None)

        equipment_type = EquipmentType.objects.get(pk=pk)
        equipment_type.label = label
        equipment_type.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        equipmentType = EquipmentType.objects.get(pk=pk)
        serialized = EquipmentTypeSerializer(equipmentType)
        return Response(serialized.data)

    def list(self, request):
        """Handle GET requests to equipmentTypes resource

        Returns:
            Response -- JSON serialized list of equipmentTypes
        """
        equipmentTypes = EquipmentType.objects.all()
        serialized = EquipmentTypeSerializer(equipmentTypes, many=True)
        return Response(serialized.data)

    def create(self, request):
        """Handle POST operations for equipmentTypes

        Returns:
            Response -- JSON serialized equipmentType instance
        """
        label = request.data.get("label", None)

        equipment_type = EquipmentType()
        equipment_type.label = label
        equipment_type.save()

        serialized = EquipmentTypeSerializer( equipment_type)
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class EquipmentTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for equipmentType creator"""

    class Meta:
        """JSON serializer for equipmentType creator"""
        model = EquipmentType
        fields = ( 'id', 'label', )
