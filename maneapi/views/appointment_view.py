"""View module for handling requests about appointments"""
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from maneapi.models import Appointment


class AppointmentView(ViewSet):
    """Viewset for appointments"""

    def update(self, request, pk=None):
        """Handle PUT requests for a appointment

        Returns:
            Response -- Empty body with 204 status code
        """
        appointment = Appointment.objects.get(pk=pk)

        # Check for invalid characters in the title
        prepaid = request.data.get("prepaid", None)
        appointment_date = request.data.get("appointment_date", None)
        stylist_id = request.data.get("stylist_id", None)

        appointment.stylist = User.objects.get(pk=stylist_id)
        appointment.prepaid = prepaid
        appointment.appointment_date = appointment_date
        appointment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        appointment = Appointment.objects.get(pk=pk)
        serialized = AppointmentSerializer(appointment)
        return Response(serialized.data)


    def list(self, request):
        """Handle GET requests to appointments resource

        Returns:
            Response -- JSON serialized list of appointments
        """
        appointments = Appointment.objects.all()
        serialized = AppointmentSerializer(appointments, many=True)
        return Response(serialized.data)

    def create(self, request):
        """Handle POST operations for appointments

        Returns:
            Response -- JSON serialized appointment instance
        """
        appointment = Appointment()
        prepaid = request.data.get("prepaid", None)
        appointment_date = request.data.get("appointment_date", None)
        stylist_id = request.data.get("stylist_id", None)

        appointment.stylist = User.objects.get(pk=stylist_id)
        appointment.prepaid = prepaid
        appointment.appointment_date = appointment_date
        appointment.save()

        serialized = AppointmentSerializer(appointment, context={'request': request})
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class AppointmentSerializer(serializers.ModelSerializer):
    """JSON serializer for appointment creator"""


    class Meta:
        """JSON serializer for appointment creator"""
        model = Appointment
        fields = ('id', 'stylist', 'prepaid', 'appointment_date',)
