from rest_framework import serializers
from .models import Property, Tenant, RentalPayments

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'type', 'address', 'num_units', 'rental_cost']
        
class TenantSerializer(serializers.ModelSerializer):
    property_name = serializers.SerializerMethodField()
    property_address = serializers.SerializerMethodField()

    class Meta:
        model = Tenant
        fields = ['id', 'property', 'property_name', 'property_address', 'name', 'phone', 'occupied_section']

    def get_property_name(self, obj):
        if obj.property:
            return obj.property.name

    def get_property_address(self, obj):
        if obj.property:
            return obj.property.address
    
    
class RentalPaymentSerializer(serializers.ModelSerializer):
    tenant_name = serializers.SerializerMethodField()
    tenant_property = serializers.SerializerMethodField()
    tenant_property_address = serializers.SerializerMethodField()
    
    class Meta:
        model = RentalPayments
        fields = ['id', 'tenant', 'tenant_name', 'tenant_property', 'tenant_property_address', 'status', 'date', 'due_date']
        
    def get_tenant_name(self, obj):
        return obj.tenant.name
    
    def get_tenant_property(self, obj):
        if obj.tenant.property:
            return obj.tenant.property.name
    
    def get_tenant_property_address(self, obj):
        if obj.tenant.property:
            return obj.tenant.property.address