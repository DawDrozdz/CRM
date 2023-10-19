from django.db import models
from .choices import Question, Type, TypeOfEveryone, TypeOfMeeting
from .managers import ManagerCategory


class Contacts(models.Model):
    choose = models.CharField(choices=TypeOfEveryone.SUM_UP, null=True, max_length=30)
    name = models.CharField(max_length=40, default='Unknown')
    NIP_numer = models.CharField(max_length=10, blank=True, null=True, default='Unknown')
    phone_number = models.CharField(max_length=9, blank=True, null=True, default='Unknown')
    email_address = models.EmailField(max_length=50, blank=True, null=True, default='Unknown')
    price = models.IntegerField(default=0)
    invoice = models.CharField(choices=Question.ANSWER, max_length=30)
    type = models.CharField(choices=Type.STATUS, max_length=30)
    objects = models.Manager()
    managers = ManagerCategory()

    def __str__(self):
        return self.name


class Customers(models.Model):
    choose = models.CharField(choices=TypeOfEveryone.SUM_UP, null=True, max_length=30)
    name = models.CharField(max_length=40, default='Unknown')
    phone_number = models.CharField(max_length=9, blank=True, null=True, default='Unknown')
    price = models.IntegerField(default=0)
    type = models.CharField(choices=Type.STATUS, max_length=30)
    managers = ManagerCategory()
    objects = models.Manager()

    def __str__(self):
        return self.name


class Interactions(models.Model):
    meeting_type = models.CharField(choices=TypeOfMeeting.SUM_UP, max_length=30)
    person_customer = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True, blank=True)
    person_contact = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, blank=True)
    meeting = models.DateField(default='2023-10-08 ')
    note = models.TextField(max_length=1000, default='Max length is 1000 words')
    managers = ManagerCategory()
    objects = models.Manager()

    def __str__(self):
        return str(self.meeting_type)


class Deals(models.Model):
    choose = models.CharField(choices=TypeOfEveryone.SUM_UP, null=True, max_length=30)
    customer = models.ManyToManyField(Customers, blank=True)
    describe = models.TextField(max_length=2500, default='Max length is 2500 words')
    managers = ManagerCategory()
    objects = models.Manager()

    def __str__(self):
        return self.choose