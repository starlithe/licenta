from django import forms
from .models import Comanda

class SearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].required = False

        self.fields['q'].widget.attrs.update(
            {'autocomplete': 'false', 'class': 'searchTerm'})


class ComandaForm(forms.ModelForm):

    class Meta:
        model = Comanda
        fields = ['name', 'phone_number', 'adress']

        # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)

        # self.fields['name'].widget.attrs.update(
        #     {'class': 'form-select'})

        # self.fields['phone_number'].widget.attrs.update(
        #     {'class': 'form-select'})

        # self.fields['adress'].widget.attrs.update(
        #     {'class': 'form-select'})

