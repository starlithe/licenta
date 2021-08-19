from django import forms 


class SearchFormPost(forms.Form):
    search_q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search_q'].required = False

        self.fields['search_q'].widget.attrs.update(
            {'class': 'searchTerm', 'autocomplete': 'false', 'type': 'search', 'placeholder': 'Cauta produse...'})
