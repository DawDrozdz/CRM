from django.db import models


class SendEmail(models.Model):
    topic = models.CharField(max_length=100)
    text = models.TextField()
    sender = models.EmailField(default='programming.sender@gmail.com')
    recipient = models.EmailField()

    def __str__(self):
        return self.topic

