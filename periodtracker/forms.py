from django import forms
from django.forms import DateInput

from .models import Period

class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ('starting_date', 'mood', 'pain', 'comment',)
        widgets = {
            'starting_date': forms.DateInput(attrs={'type': 'date'}),
            'mood': forms.Select(attrs={'class':'form-control'}),
            'pain': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class':'form-control'}),
        }



class EditPeriodForm(forms.ModelForm):

    class Meta:
        model = Period
        fields = ('ending_date',)
        widgets = {
            'ending_date': forms.DateInput(attrs={'type': 'date','placeholder':'noch nicht bekannt'}),
        }

