from warnings import filters
from rest_framework import generics
from .models import Property, RentalPayments, Tenant
from .serializers import PropertySerializer, TenantSerializer, RentalPaymentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import PropertyFilter
from rest_framework.permissions import IsAuthenticated

class PropertyAdd(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'pk'
    
class PropertyList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = PropertyFilter
    ordering_fields = ['rental_cost', 'type', 'address']
    
class AddTenant(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    
class viewTenant(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    lookup_field = 'pk'
    
class TenantList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    
    
class AddPayment(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RentalPaymentSerializer
    
    def get_queryset(self):
        tenant_id = self.kwargs('tenant_id')
        return RentalPayments.objects.filter(tenant__id=tenant_id)
        
class ViewPayment(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RentalPaymentSerializer
    queryset = RentalPayments.objects.all()
    lookup_field = 'pk'
    
    
class PaymentList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = RentalPayments.objects.all()
    serializer_class = RentalPaymentSerializer
