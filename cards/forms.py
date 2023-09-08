from django import forms


class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(widget=forms.HiddenInput)
    quality = forms.IntegerField(widget=forms.HiddenInput, required=False)
