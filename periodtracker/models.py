from django.db import models

# Create your models here.


from django.conf import settings
from django.db import models
from django.utils import timezone


class Period(models.Model):

    MOODS =  [
        ("Glücklich", "Glücklich"),
        ("Krank", "Krank"),
        ("Wütend", "Wütend"),
        ("Müde", "Müde"),
        ("Hungrig", "Hungrig"),
    ]

    PAINS = [
        ("keine", "keine"),
        ("leicht", "leicht"),
        ("regulär", "regulär"),
        ("stark", "stark"),

    ]

    mood = models.CharField(max_length=50, default='3', choices = MOODS)
    comment=models.CharField(max_length=250, default='')
    pain = models.CharField(max_length=50, default='2', choices = PAINS)
    starting_date = models.DateField()
    ending_date = models.DateField(null=True)

    def __str__(self):
        return f'Period {self.id}: {self.mood} {self.pain} {self.starting_date} {self.ending_date} {self.comment}'