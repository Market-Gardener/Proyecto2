from django import forms

class userForm(forms.Form):
    pisina = forms.ChoiceField()
    price = forms.IntegerField()