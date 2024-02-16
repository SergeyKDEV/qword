from django import forms

from .models import Word


class WordForm(forms.ModelForm):
    word = forms.CharField(
        max_length=30,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'СЛОВО'})
    )
    translate = forms.CharField(
        max_length=30,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'ПЕРЕВОД'})
    )

    class Meta:
        model = Word
        fields = ('word', 'translate',)
