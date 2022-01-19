from rest_framework import serializers

from core.models import Workplace, Booking


class WorkplaceSerializer(serializers.ModelSerializer):
    """Serializer for workplace objects"""

    class Meta:
        model = Workplace
        fields = ('id',)
        read_only_fields = ('id',)


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for booking objects"""

    class Meta:
        model = Booking
        fields = ('id', 'user', 'workplace', 'datetime_from', 'datetime_to')
        read_only_fields = ('id', 'user',)
