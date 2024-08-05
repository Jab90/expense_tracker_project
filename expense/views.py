from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from .models import Expense

class HomePage(TemplateView):
    """
    Displays Home page"
    """
    template_name = "expense/index.html"

def expense_tool(request):
    return render(request, 'expense/expense_tool.html')