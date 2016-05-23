from django.db import models
from django.forms import ModelForm
import datetime

# Create your models here.

class Stock(models.Model):
    ticker = models.CharField(max_length=32)

class Report(models.Model):
    report_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)
    plotly_url = models.URLField(max_length=200)
    notes = models.TextField()
    stocks = models.ManyToManyField(Stock, blank=True)
    start_date = models.DateTimeField('start date', default=datetime.date.today, blank=True)
    end_date = models.DateTimeField('end date', default=datetime.date.today, blank=True)

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker']

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['report_name', 'notes', 'stocks', 'start_date', 'end_date']