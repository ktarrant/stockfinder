from report.models import Stock, StockPlot, Report
from django.forms import ModelForm

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker']

class StockPlotForm(ModelForm):
    class Meta:
        model = StockPlot
        fields = ['plot_stock', 'caption', 'description', 'start_date', 'end_date']

    def clean(self):
        cleaned_data = self.cleaned_data
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if end_date.toordinal() - start_date.toordinal() < 60:
            raise ValidationError('Time span must be at least 60 days')

        return cleaned_data

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['report_name', 'stock_plots']