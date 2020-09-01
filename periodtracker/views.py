from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory, DateInput
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PeriodForm
from .forms import EditPeriodForm
from .models import Period
from django.utils import timezone


@login_required
def period_list(request):
    periods = Period.objects.all()
    return render(request, 'periodtracker/period_list.html', {'periods': periods})

#PeriodForm = modelform_factory(Period, exclude=[], widgets={'starting_date': DateInput(attrs = {'type' : 'date'})})

@login_required
def period_new(request):
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            period = form.save(commit=False)
            period.save()
            return redirect('period_list')
    else:
        form = PeriodForm()
    return render(request, 'periodtracker/period_new.html', {'form': form})

#EditPeriodForm = modelform_factory(Period, exclude=['mood','comment','pain','starting_date'])

@login_required
def period_edit(request,pk):
    period = get_object_or_404(Period, pk=pk)
    if request.method == "POST":
        form = EditPeriodForm(request.POST, instance=period)
        if form.is_valid():
            period = form.save(commit=False)
            period.save()
            return redirect('period_list')
    else:
        form = EditPeriodForm(instance=period)
    return render(request, 'periodtracker/period_edit.html', {'form': form})

@login_required
def period_delete(request,pk):
    pk= pk
    b = Period.objects.get(pk=pk)
    b.delete()
    return redirect('period_list')

