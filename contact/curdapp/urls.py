from django.urls import path
from .views import ContactFormView, ContactFormDetails

urlpatterns = [
    path('contact/', ContactFormView.as_view(), name="contacts"),
    path('contact/<int:id>/', ContactFormDetails.as_view(), name="contact-detail"),
]
