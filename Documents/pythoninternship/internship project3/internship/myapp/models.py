from django.db import models

# # Create your models here.
# class Wordcount(models.Model):
#     text=models.TextField(max_length=5000000)
#     word_count=models.IntegerField()
    

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Others', 'Others'),
    ]
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)


