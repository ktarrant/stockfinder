from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from stock.models import Stock, StockPlot
# from report.forms import ReportForm

# def update_report_plot(report):
#     # Create the plot
#     df = web.DataReader("scty", 'yahoo', report.start_date, report.end_date)
#     fig = candlestick.Candlestick(df)
#     report.plotly_url = plot(fig)

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