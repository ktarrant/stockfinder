from django.db import models
from datetime import datetime

# Create your models here.
class Stock(models.Model):           
    ticker = models.CharField(max_length=32, primary_key=True)
    default_plot = models.ManyToManyField('StockPlot')
    def __str__(self):
        return self.ticker

class StockPlot(models.Model):
    # Editable fields
    plot_stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField('start date', default=datetime.now)
    end_date = models.DateTimeField('end date', default=datetime.now)

    # Non-editable fields
    pub_date = models.DateTimeField('date published', auto_now_add=True, editable=False)
    edit_date = models.DateTimeField('date edited', auto_now_add=True, editable=False)
    plotly_url = models.URLField(max_length=200, editable=False)
    plotly_filename = models.CharField(max_length=200, editable=False)