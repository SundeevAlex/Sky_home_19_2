from django.forms import ModelForm
from catalog.models import Product
from django import forms

prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        for el in prohibited_words:
            if el in cleaned_name:
                raise forms.ValidationError('Нельзя использовать это слово!')
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data['description']
        for el in prohibited_words:
            if el in cleaned_description:
                raise forms.ValidationError('Нельзя использовать это слово!')
        return cleaned_description
