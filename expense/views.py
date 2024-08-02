from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Expense

class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = "expense/index.html"


    