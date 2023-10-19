from django.db import models


class Question(models.Model):
    #Czy bierze fakture
    ANSWER = (
        ('YES', 'YES'),
        ('NO', 'NO')
    )


class Type(models.Model):
    #Jaki jest rodzaj klienta/Współpracownika
    STATUS = (
        ('LEAD', 'LEAD'),
        ('CONTACT AGAIN', 'CONTACT AGAIN'),
        ('DECIDED', 'DECIDED'),
        ('SUCCESS', 'SUCCESS')
    )


class TypeOfMeeting(models.Model):
    #Typ spotkania
    SUM_UP = (
        ('SHOWING THE APARTMENT', 'SHOWING THE APARTMENT'),
        ('VALUATION OF RENOVATION', 'VALUATION OF RENOVATION'),
        ('CONSTRUCTION INSPECTION', 'CONSTRUCTION INSPECTION'),
        ('PICKING UP THE MOTORCYCLE', 'PICKING UP THE MOTORCYCLE')
    )


class TypeOfEveryone(models.Model):
    #Jaki jest rodzaj zadania/oferty/klienta
    SUM_UP = (
        ('STATES', 'STATES'),
        ('MOTORCYCLE', 'MOTORCYCLE')
    )
