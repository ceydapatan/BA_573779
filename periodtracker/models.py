from django.conf import settings
from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


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
    pain = models.CharField(max_length=52, default='2', choices = PAINS,null=True)
    start_time = models.DateField(null=True)
    end_time = models.DateField(null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return f'Period {self.id}: {self.mood} {self.pain} {self.start_time}  {self.end_time} {self.comment}'


    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.commment} </a>'