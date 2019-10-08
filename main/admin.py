from django.contrib import admin
from django.http import HttpResponse

from . import models

import csv


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'state')
    list_filter = ('name', 'phone', 'email', 'state')
    search_fields = ('name', )
    
    def export_company_csv(self, request, queryset, **kwargs):
        model_class = models.Company
        meta = model_class._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        
        return response
    
    export_company_csv.short_description = "Export companies list to csv"
    actions = [export_company_csv]
