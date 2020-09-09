from django import forms
from django.forms import DateInput

from .models import Period

class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ('start_time', 'mood', 'pain', 'comment',)
        widgets = {
            'start_time': forms.DateInput(attrs={'type': 'date'}),
            'mood': forms.Select(attrs={'class':'form-control'}),
            #'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),


            'pain': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class':'form-control'}),
        }



class EditPeriodForm(forms.ModelForm):

    class Meta:
        model = Period
        fields = ('end_time',)
        widgets = {
            'end_time': forms.DateInput(attrs={'type': 'date', 'placeholder': 'noch nicht bekannt'}),
        }

