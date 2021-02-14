from django import forms

class SearchForm(forms.Form):
    search=forms.CharField(label='username', max_length=100)
