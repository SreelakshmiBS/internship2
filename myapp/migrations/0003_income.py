# Generated by Django 5.1.6 on 2025-02-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_expense_delete_wordcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Salary', 'Salary'), ('Extra inc0me', 'Extra income'), ('Others', 'Others')], max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
