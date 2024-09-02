from random import choice
from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta

class Property(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    num_units = models.SmallIntegerField()
    rental_cost = models.DecimalField(decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.name
    
class Tenant(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, null=True, unique=True)
    occupied_section = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name
    
class RentalPayments(models.Model):
    STATUS = (
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    )
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='payments')
    status = models.CharField(max_length=6, choices=STATUS, default='unpaid')
    date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True)

    class Meta:
        unique_together = ['tenant', 'date']
    
    def save(self, *args, **kwargs):
        if not self.due_date:
            today = date.today()
            next_month = today + relativedelta(months=1)
            self.due_date = next_month.replace(day=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tenant.name