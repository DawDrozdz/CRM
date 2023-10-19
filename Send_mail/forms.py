from .models import SendEmail
from django.forms import ModelForm


class SendEmailForm(ModelForm):
    class Meta:
        model = SendEmail
        fields = ['sender', 'recipient', 'topic', 'text', 'sender']