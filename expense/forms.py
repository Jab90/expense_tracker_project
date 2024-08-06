from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm): 
    """
    This for has been created so the user can add and edit an expense
    """
    class Meta: 

        model = Expense
        fields = ['item', 'amount', 'currency']

        widgets = {
            'item': forms.TextInput(attrs={'placeholder': 'Enter item'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount', 'min': '0', 'step': '0.01'}),
            'currency': forms.Select(attrs={'placeholder': 'Enter currency'}),
        }