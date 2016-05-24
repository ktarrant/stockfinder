from django.db import models
from django.forms import ModelForm
from datetime import datetime

# Create your models here.

class Stock(models.Model):           
    ticker = models.CharField(max_length=32, primary_key=True)
    def __str__(self):
        return self.ticker

class Plot(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    plotly_url = models.URLField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    start_date = models.DateTimeField('start date', 
        default=lambda:datetime.fromordinal(datetime.now().toordinal() - 200))
    end_date = models.DateTimeField('end date', default=datetime.now, blank=True)
    caption = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

class Report(models.Model):
    report_name = models.CharField(max_length=200)
    plots = models.ManyToManyField(Plot, blank=True)
    def __str__(self):
        return "Report: {}".format(self.report_name)

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker']

class PlotForm(ModelForm):
    class Meta:
        model = Plot
        fields = []

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['report_name', 'notes', 'stocks', 'start_date', 'end_date']