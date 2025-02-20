# from django.contrib import admin
# from django.urls import path, include
# from myapp import views  # Ensure this import is correct

# urlpatterns = [
#     path('', views.count_words, name='home'),
#     path('count_words/', views.count_words, name='count_words'),  # Add this!
#     path('admin/', admin.site.urls),
#     path('myapp/', include('myapp.urls')),  # Include wordcounter app URLs
# ]

from django.urls import path
from myapp import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'), 
    # path('expense_list', views.expense_list, name='expense_list'),
    # path('admin/', admin.site.urls),
    # path('myapp', include('myapp.urls')),
    path('expense_list/', views.expense_list, name='expense_list'),
    path('add_expense/', views.add_expense, name='add_expense')
]