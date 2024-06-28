from django.forms import ModelForm, BooleanField
from catalog.models import Product, Version
from django import forms

prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    # pass
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Product
        exclude = ('owner',)
        # fields = '__all__'

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


class VersionForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
