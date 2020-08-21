from django.forms import modelform_factory
from django.shortcuts import render, redirect
from .models import Period
from django.utils import timezone
from .forms import PeriodForm


def period_list(request):
    periods = Period.objects.filter(starting_date__lte=timezone.now()).order_by('starting_date')
    return render(request, 'periodtracker/period_list.html', {'periods': periods})

PeriodForm = modelform_factory(Period, exclude=[])

def period_new(request):
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            period = form.save(commit=False)
            period.starting_date = timezone.now()
            period.save()
            return redirect('period_list')
    else:
        form = PeriodForm()
    return render(request, 'periodtracker/period_new.html', {'form': form})