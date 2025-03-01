from .views import send_email_view
from django.urls import path

urlpatterns = [
    path('', send_email_view, name='send_email'),
]
