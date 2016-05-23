from django.contrib import admin

# Register your models here.
from report.models import Stock, Report

admin.site.register(Stock)
admin.site.register(Report)