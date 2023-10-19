from django.db import models
from Backend.choices import TypeOfEveryone


class Tasks(models.Model):
    choose = models.CharField(choices=TypeOfEveryone.SUM_UP, null=True, max_length=30)
    note = models.TextField(max_length=2500, default='Max length is 2500 words')
    objects = models.Manager()

    def __str__(self):
        return self.choose
