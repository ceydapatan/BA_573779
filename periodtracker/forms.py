from django import forms

from .models import Period


class PeriodForm(forms.ModelForm):

    class Meta:
        model = Period
        fields = ('starting_date','pain','mood','comment')