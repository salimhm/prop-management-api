from django.core.mail import send_mail
from datetime import date
from .models import RentalPayments

def send_due_rental_payments():
    today = date.today()
    due_payments = RentalPayments.objects.filter(status='unpaid', due_date__lte=today)

    for payment in due_payments:
        tenant_name = payment.tenant.name
        tenant_email = payment.tenant.email
        property_name = payment.tenant.property.name
        
        subject = f'Payment due: {property_name}'
        message = f'Dear {tenant_name},\n\nYour payment for {property_name} is overdue, please settle the amount as soon as possible.\n\nThanks.'
        from_email = 'noreply@bestproperties.com'
        recipient_list = [tenant_email]
        print('Payment=>', payment.due_date)
        print(f"Sending email to: {tenant_email} for payment due on {payment.due_date}")
        
        if send_mail(subject, message, from_email, recipient_list) != 0:
            print('Email sent successfully!')
