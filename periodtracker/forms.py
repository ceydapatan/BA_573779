from django import forms
from django.forms import DateInput

from .models import Period


class PeriodForm(forms.ModelForm):

    class Meta:
        model = Period
        fields = ('starting_date', 'mood', 'pain', 'comment',)
        widgets = {
            'starting_date': DateInput(attrs={'type': 'date'})
        }

