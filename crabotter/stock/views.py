from django.shortcuts import render
from report.models import Stock, StockPlot
# from report.forms import ReportForm
from datetime import datetime
import report.candlestick as candlestick
import pandas_datareader.data as web
import plotly.tools as tls
from plotly.plotly import plot

# Create your views here.

endtime = 
starttime = 
df = web.DataReader("scty", 'yahoo', starttime, endtime)
fig = candlestick.Candlestick(df)
url = plot(fig)
embedHtml = tls.get_embed(url)