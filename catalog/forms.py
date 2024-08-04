from django.forms import ModelForm, BooleanField
from catalog.models import Product, Version
from django import forms

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        #fields = '__all__'
        #exclude = ('',)
        fields = ('name', 'description', 'image', 'category', 'price')

    def clean_name(self ):
        name = self.cleaned_data.get('name')
        for i in forbidden_words:
            if i in name.lower():
                raise forms.ValidationError(
                    f"Поле не должно содержать запрещенные слова: {', '.join(forbidden_words)}"
                )
        return name

    def clean_description(self ):
        description = self.cleaned_data.get('description')
        for i in forbidden_words:
            if i in description.lower():
                raise forms.ValidationError(
                    f"Описание не должно содержать запрещенные слова: {', '.join(forbidden_words)}"
                )
        return description


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'version_number', 'version_name', 'current_sign')