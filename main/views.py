from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_filters.views import FilterView

from .models import Company
from . import forms
from . import filters


class IndexView(FilterView):
    model = Company
    context_object_name = 'companies'
    template_name = 'main/index.html'
    paginate_by = 5
    filterset_class = filters.CompanyFilter


class CompanyCreateView(CreateView):
    model = Company
    form_class = forms.CompanyForm
    success_url = reverse_lazy('main:index')
    template_name = 'main/company_create.html'
    context_object_name = 'company'
    

class CompanyUpdateView(UpdateView):
    model = Company
    form_class = forms.CompanyForm
    success_url = reverse_lazy('main:index')
    template_name = 'main/company_update.html'
    context_object_name = 'company'
    

class CompanyDeleteView(DeleteView):
    model = Company
    form_class = forms.CompanyForm
    success_url = reverse_lazy('main:index')
    template_name = 'main/company_delete.html'
    context_object_name = 'company'
