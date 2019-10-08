from django.forms import ModelForm

from . import models


class CompanyForm(ModelForm):
    class Meta:
        model = models.Company
        fields = '__all__'
