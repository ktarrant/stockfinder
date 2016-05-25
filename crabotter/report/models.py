from django.db import models
from datetime import datetime
from stock.models import StockPlot

# Create your models here.
class Report(models.Model):
    report_name = models.CharField(max_length=200)
    stock_plots = models.ManyToManyField(StockPlot, blank=True)
    def __str__(self):
        return "Report: {}".format(self.report_name)