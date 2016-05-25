from django.shortcuts import render, Http404
from stock.models import Stock, StockPlot
from datetime import datetime
import stock.candlestick as candlestick
import pandas_datareader
import pandas_datareader.data as web
import plotly.tools as tls
from plotly.plotly import plot

# Create your views here.
def home(request):
    return detail(request, 'aapl')

def detail(request, ticker):
    tickerClean = ticker.lower()
    try:
        stock = Stock.objects.get(ticker=tickerClean)
    except Stock.DoesNotExist:
        # Create the stock plot
        plotRange = 200
        endtime = datetime.now()
        starttime = datetime.fromordinal(endtime.toordinal() - plotRange)
        try:
            df = web.DataReader(tickerClean, 'yahoo', starttime, endtime)
        except pandas_datareader._utils.RemoteDataError:
            raise Http404("Ticker symbol not found: {}".format(ticker))
        stock = Stock.objects.create(ticker=tickerClean)
        fig = candlestick.Candlestick(df)
        plotly_filename = "stock/{}".format(tickerClean)
        url = plot(fig, filename=plotly_filename, auto_open=False)
        stockPlot = stock.default_plot.create(
            plot_stock=stock,
            title="Movement of {} over last {} days".format(ticker.upper(), plotRange),
            start_date=starttime,
            end_date=endtime,
            pub_date=datetime.now(),
            edit_date=datetime.now(),
            plotly_url=url,
            plotly_filename=plotly_filename)

    return render(request, 'stock/detail.html', {"stock": stock, 'plots': stock.default_plot.all()})