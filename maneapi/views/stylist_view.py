"""View module for handling requests about stylists"""
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from maneapi.models import Customer, Equipment

"""
Users (un:pwd)
-----------------
meg:ducharme
madi:peper
ryna:tanay
"""


class StylistView(ViewSet):
    """Viewset for stylists"""

    def update(self, request, pk=None):
        """Handle PUT requests for a stylist

        Returns:
            Response -- Empty body with 204 status code
        """
        stylist = request.auth.user

        # Check for invalid characters in the title
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        email = request.data["email"]

        stylist.first_name = first_name
        stylist.last_name = last_name
        stylist.email = email

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        stylist = request.auth.user
        serialized = StylistSerializer(stylist)
        return Response(serialized.data)


    def list(self, request):
        """Handle GET requests to stylists resource

        Returns:
            Response -- JSON serialized list of stylists
        """
        stylists = User.objects.all()
        serialized = StylistSerializer(stylists, many=True)
        return Response(serialized.data)

class StylistCustomerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Customer
        fields = ('id', 'stylist', 'name', 'date_created', 'appointments')

class StylistEquipmentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Equipment
        fields =  (
            'id', 'stylist', 'manufacturer', 'cost',
            'type', 'purchase_date'
        )

class StylistSerializer(serializers.ModelSerializer):
    """JSON serializer for stylist creator"""
    customers = StylistCustomerSerializer(many=True)
    equipment = StylistEquipmentSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'customers', 'equipment', )
