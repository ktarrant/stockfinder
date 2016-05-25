from django.shortcuts import render
from report.models import Stock, StockPlot
from datetime import datetime
import report.candlestick as candlestick
import pandas_datareader.data as web
import plotly.tools as tls
from plotly.plotly import plot

# Create your views here.

def stock(request, ticker):
    tickerClean = ticker.lower()
    try:
        stock = Stock.objects.get(ticker=tickerClean)
    except Stock.DoesNotExist:
        # Create the stock plot
        endtime = datetime.today()
        starttime = datetime.fromordinal(endtime.toordinal() - 365)
        try:
            df = web.DataReader(tickerClean, 'yahoo', starttime, endtime)
        except RemoteDataError:
            raise Http404("Ticker symbol not found: {}".format(ticker))
        stock = Stock.objects.create(ticker=tickerClean)
        fig = candlestick.Candlestick(df)
        plotly_filename = "stock/{}".format(tickerClean)
        url = plot(fig, filename=plotly_filename, auto_open=False)
        stockPlot = stock.default_plot.create(
            plot_stock=stock,
            start_date=datetime.fromordinal(endtime.toordinal() - 365),
            end_date=datetime.now(),
            pub_date=datetime.now(),
            edit_date=datetime.now(),
            plotly_url=url,
            plotly_filename=plotly_filename)

    return render(request, 'report/stock.html', {"stock": stock, 'plots': stock.default_plot.all()})