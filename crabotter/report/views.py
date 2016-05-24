from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from report.models import Stock, StockPlot
# from report.forms import ReportForm
from datetime import datetime
import report.candlestick as candlestick
import pandas_datareader.data as web
import plotly.tools as tls
from plotly.plotly import plot

# endtime = 
# starttime = 
# df = web.DataReader("scty", 'yahoo', starttime, endtime)
# fig = candlestick.Candlestick(df)
# url = plot(fig)
# embedHtml = tls.get_embed(url)

# def update_report_plot(report):
#     # Create the plot
#     df = web.DataReader("scty", 'yahoo', report.start_date, report.end_date)
#     fig = candlestick.Candlestick(df)
#     report.plotly_url = plot(fig)

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

    plots = [tls.get_embed(stockPlot.plotly_url) for stockPlot in stock.default_plot.all()]
    return render(request, 'report/stock.html', {'plots': plots, "stock": stock})

# def new(request):
#     if request.method == "POST":
#         form = ReportForm(request.POST)
#         if form.is_valid():
#             report = form.save(commit=False)
#             report.author = request.user
#             report.pub_date = datetime.now()
#             update_report_plot(request, report)
#             report.save()
#             return redirect('report_detail', pk=report.pk)
#     else:
#         form = ReportForm()
#     return render(request, 'report/new.html', {'form': form})

# def edit(request, pk):
#     report = get_object_or_404(Report, pk=pk)
#     if request.method == "POST":
#         form = ReportForm(request.POST, instance=report)
#         if form.is_valid():
#             report = form.save(commit=False)
#             update_report_plot(report)
#             report.save()
#             return redirect('report_detail', pk=report.pk)
#     else:
#         form = ReportForm(instance=report)
#     embedHtml = tls.get_embed(report.plotly_url)
#     return render(request, 'report/edit.html', {'form': form, 'plot': embedHtml})