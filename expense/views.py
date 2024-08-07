from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import generic
from django.contrib import messages
from .models import Expense
from .forms import ExpenseForm

class HomePage(TemplateView):
    """
    Displays Home page"
    """
    template_name = "expense/index.html"

def expense_tool(request):

    expenses = Expense.objects.filter(user=request.user)
    total_amount = sum(expense.amount for expense in expenses)
    return render(request, 'expense/expense_tool.html',{
        "expenses": expenses,
        "total_amount": total_amount,
    })

def add(request):
    

    if request.method == 'POST':
        expense_form = ExpenseForm(data=request.POST)
        if expense_form.is_valid():
            expense = expense_form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Expense added!'
            )
            return redirect('expense_tool')
    else: 
        expense_form = ExpenseForm()

    return render(request, 'expense/add.html', {'expense_form': expense_form})


def edit(request, edit_id):

    expense = get_object_or_404(Expense, pk=edit_id, user=request.user)

    if request.method == "POST": 
        expense_form = ExpenseForm(data=request.POST, instance=expense)
        if expense_form.is_valid():
            expense_form.save()
            messages.success(request, 'Expense Updated!')
            return HttpResponseRedirect(reverse("expense_tool"))
        else:
            messages.error(request, "Error updating expense!")
    else: 
        expense_form = ExpenseForm(instance=expense)
    
    return render(
        request, 'expense/edit.html',
        {'form': expense_form, 'edit_id': edit_id}
    )

    return render(request, 'expense/edit.html')

def delete(request, expense_id):

    expense = get_object_or_404(Expense, pk=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, "Expense Deleted!")
    
    return redirect("expense_tool")