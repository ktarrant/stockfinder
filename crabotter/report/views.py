from django.shortcuts import render
from django.http import HttpResponse
from report.models import ReportForm

# import datetime
# import report.candlestick as candlestick
# import pandas_datareader.data as web
# import plotly.tools as tls
# from plotly.plotly import plot

# endtime = datetime.date.today()
# starttime = datetime.date.fromordinal(endtime.toordinal() - 365)
# df = web.DataReader("scty", 'yahoo', starttime, endtime)
# fig = candlestick.Candlestick(df)
# url = plot(fig)
# embedHtml = tls.get_embed(url)

def new(request):
    form = ReportForm()
    return render(request, 'report/report_edit.html', {'form': form})

def detail(request):
    context = {'plot': ""}
    return render(request, 'report/index.html', context)