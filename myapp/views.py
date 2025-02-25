from django.shortcuts import render, redirect
from .models import Expense,Income
from .forms import ExpenseForm,IncomeForm


def add_expense(request):        #you can add your expense
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})      #shows the list of your expense

def home(request):
    return render(request, "myapp/home.html")

def add_income(request):        #add your income
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    else:
        form = IncomeForm()
    return render(request, 'add_income.html', {'form': form})

def income_list(request):
    incomes = Income.objects.all()          #your income listed here
    return render(request, 'income_list.html', {'incomes': incomes})
