from django.test import TestCase
from unittest.mock import patch
from .models import Property, Tenant, RentalPayments
from .utils import send_due_rental_payments
from datetime import date
from django.core import mail
from dateutil.relativedelta import relativedelta

class RentalPaymentTestCase(TestCase):

    def setUp(self):
        self.property = Property.objects.create(
            name="Best Apartments",
            type="Apartment",
            address="123 Main Street",
            num_units=10,
            rental_cost=1000.00
        )
        
        self.tenant = Tenant.objects.create(
            property=self.property,
            name="John Doesss",
            phone="1234567890",
            email='JohnDoesss@lol.com',
            occupied_section="Unit 1"
        )
        
        today = date.today()
        next_month = today + relativedelta(months=1)
        due_date = next_month.replace(day=1)
        self.rental_payment = RentalPayments.objects.create(
            tenant=self.tenant,
            status='unpaid',
            date=date(2024, 9, 22),
            due_date=due_date
        )

    @patch('django.core.mail.send_mail')
    def test_send_due_notifs(self, mock_send_mail):
        send_due_rental_payments()
        self.assertEqual(len(mail.outbox), 1)