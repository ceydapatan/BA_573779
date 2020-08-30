from django.db import models

# Create your models here.
from django.db import models


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

    mood = models.CharField(max_length=50, default='3', choices = MOODS, null=True)
    comment=models.CharField(max_length=251, default='',null=True)
    pain = models.CharField(max_length=51, default='2', choices = PAINS,null=True)
    starting_date = models.DateField(null=True)
    #ending_date= models.DateField(null=True)


    def __str__(self):
        return f'Period {self.id}: {self.mood} {self.pain} {self.starting_date}  {self.comment}'