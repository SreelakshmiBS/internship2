# from django import forms

# class WordCountForm(forms.Form):
#     text = forms.CharField(widget=forms.Textarea, label="Enter your text")
from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'category']