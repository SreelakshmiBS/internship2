
from django.urls import path
from myapp import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'), 
    path('expense_list/', views.expense_list, name='expense_list'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('add_income/', views.add_income, name='add_income'),
    path('income_list/', views.income_list, name='income_list')
]
