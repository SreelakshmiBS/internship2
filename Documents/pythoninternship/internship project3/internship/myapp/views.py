
# from django.shortcuts import render
# from forms import WordCountForm
# from .models import WordCount

# def count_words(request):
#     word_count = None
#     form = WordCountForm()

#     if request.method == 'POST':
#         form = WordCountForm(request.POST)
#         if form.is_valid():
#             text = form.cleaned_data['text']
#             word_count = len(text.split()) 

#             WordCount.objects.create(text=text, word_count=word_count)

#     return render(request, 'count.html', {'form': form})
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

def home(request):
    return render(request, "myapp/home.html")



