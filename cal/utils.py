from datetime import datetime, timedelta
from calendar import HTMLCalendar


import day as day

from periodtracker.models import Period





class Calendar(HTMLCalendar):

	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	def formatday(self, day, periods):
		periods_per_day = periods.filter( start_time__year=self.year, start_time__month=self.month, start_time__day=day)
		end_per_day = periods.filter( end_time__year=self.year, end_time__month=self.month, end_time__day=day)
		d = ''
		for period in periods_per_day:
			d += f'<li> {"🩸"} </li>'

		for period in end_per_day:
			d += f'<li> {"🌸"} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	def formatweek(self, theweek,periods):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, periods)
		return f'<tr> {week} </tr>'

	def period_list(request):
		periods = Period.objects.filter(author=request.user)
		return periods

	def formatmonth(self, withyear=True):
		#period = Period.objects.filter(author=request.user)
		period = Period.objects.all()





		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, period)}\n'
		return cal