from django import forms
from .models import UploadedFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']


class QueryBuilderForm(forms.Form):
    name = forms.CharField(required=False, label='Name')
    year_founded = forms.IntegerField(required=False, label='Year Founded')
    industry = forms.CharField(required=False, label='Industry')
    locality = forms.CharField(required=False, label='Locality')
    country = forms.CharField(required=False, label='Country')

