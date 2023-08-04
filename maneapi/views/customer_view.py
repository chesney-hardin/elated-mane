"""View module for handling requests about customers"""
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from maneapi.models import Customer


class CustomerView(ViewSet):
    """Viewset for customers"""

    def update(self, request, pk=None):
        """Handle PUT requests for a customer

        Returns:
            Response -- Empty body with 204 status code
        """
        customer = Customer.objects.get(pk=pk)

        # Check for invalid characters in the title
        stylist_id = request.data["stylist_id"]
        name = request.data["name"]

        customer.stylist = User.objects.get(pk=stylist_id)
        customer.name = name
        customer.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        customer = Customer.objects.get(pk=pk)
        serialized = CustomerSerializer(customer)
        return Response(serialized.data)


    def list(self, request):
        """Handle GET requests to customers resource

        Returns:
            Response -- JSON serialized list of customers
        """
        customers = Customer.objects.all()
        serialized = CustomerSerializer(customers, many=True)
        return Response(serialized.data)

    def create(self, request):
        """Handle POST operations for customers

        Returns:
            Response -- JSON serialized customer instance
        """
        customer = Customer()
        customer.stylist = User.objects.get(pk=request.data["stylist_id"])
        customer.name = request.data["name"]
        customer.save()

        serialized = CustomerSerializer(customer, context={'request': request})
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class CustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for customer creator"""


    class Meta:
        """JSON serializer for customer creator"""
        model = Customer
        fields = ('id', 'stylist', 'name', 'date_created',)
