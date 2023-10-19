from django.urls import path
from .views import mail_sender, previous_messages, remove_mails

urlpatterns = [
    path('send_mail/', mail_sender, name='mail_sender'),
    path('previous_messages/', previous_messages, name='previous_messages'),
    path('remove_messages/<int:pk>/', remove_mails, name='remove_mails'),


]
