from django import forms

class HistoryForm(forms.Form):
	text = forms.CharField()