from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from core.models import Workplace, Booking
from booking import serializers


class WorkplaceViewSet(viewsets.ModelViewSet):
    """Base viewset for workplace"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.WorkplaceSerializer
    queryset = Workplace.objects.all()

    def get_queryset(self):
        """Return objects"""
        datetime_from = self.request.query_params.get('datetime_from')
        datetime_to = self.request.query_params.get('datetime_to')
        queryset = self.queryset

        if not datetime_from or not datetime_to:
            return queryset.order_by('id').distinct()

        
        return queryset.exclude(
            booking__datetime_from__gte=datetime_from,
            booking__datetime_to__lte=datetime_to
        ).order_by('id').distinct()


class BookingViewSet(viewsets.ModelViewSet):
    """Base viewset for booking"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.BookingSerializer
    queryset = Booking.objects.all()

    def get_queryset(self):
        """Retrieve the bookings"""
        workplace = self.request.query_params.get('workplace')
        queryset = self.queryset

        if workplace:
            queryset = queryset.filter(workplace=workplace)
        
        return queryset.order_by('id').distinct()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)
