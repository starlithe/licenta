from django import forms

class SearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].required = False

        self.fields['q'].widget.attrs.update(
            {'autocomplete': 'false', 'class': 'searchTerm'})
