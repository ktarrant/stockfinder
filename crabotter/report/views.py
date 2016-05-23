from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from report.models import Report, ReportForm
from datetime import datetime
import report.candlestick as candlestick
import pandas_datareader.data as web
import plotly.tools as tls
from plotly.plotly import plot

# endtime = datetime.date.today()
# starttime = datetime.date.fromordinal(endtime.toordinal() - 365)
# df = web.DataReader("scty", 'yahoo', starttime, endtime)
# fig = candlestick.Candlestick(df)
# url = plot(fig)
# embedHtml = tls.get_embed(url)

def update_report_plot(report):
    # Create the plot
    df = web.DataReader("scty", 'yahoo', report.start_date, report.end_date)
    fig = candlestick.Candlestick(df)
    report.plotly_url = plot(fig)
    

def new(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.author = request.user
            report.pub_date = datetime.now()
            update_report_plot(request, report)
            report.save()
            return redirect('report_detail', pk=report.pk)
    else:
        form = ReportForm()
    return render(request, 'report/new.html', {'form': form})

def edit(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            report = form.save(commit=False)
            update_report_plot(report)
            report.save()
            return redirect('report_detail', pk=report.pk)
    else:
        form = ReportForm(instance=report)
    embedHtml = tls.get_embed(report.plotly_url)
    return render(request, 'report/edit.html', {'form': form, 'plot': embedHtml})