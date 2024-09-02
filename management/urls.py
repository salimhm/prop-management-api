from django.urls import path
from . import views

urlpatterns = [
    path('api/property/add/', views.PropertyAdd.as_view(), name='add-property'),
    path('api/property/<int:pk>/', views.PropertyDetail.as_view(), name='property-detail'),
    path('api/property/', views.PropertyList.as_view(), name='view-properties'),
    path('api/tenant/add/', views.AddTenant.as_view(), name='add-tenant'),
    path('api/tenant/', views.TenantList.as_view(), name='view-tenants'),
    path('api/tenant/<int:pk>/', views.viewTenant.as_view(), name='view-tenant'),
    path('api/payments/add/', views.AddPayment.as_view(), name='add-payment'),
    path('api/payments/', views.PaymentList.as_view(), name='view-payments'),
    path('api/payments/<int:pk>/', views.ViewPayment.as_view(), name='view-payment'),
]