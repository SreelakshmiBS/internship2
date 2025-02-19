

from django.urls import path
from myapp import views 


urlpatterns = [
    path('',views.home,name='home'),  
    path('post_list',views.post_list, name='post_list'),
    path('post_create/',views.post_create, name='post_create'),
    path('post_remove/<int:post_id>/',views.post_remove, name='post_remove'),
    path('post_edit/<int:post_id>/',views.post_edit, name='post_edit'),
    path('post_view/<int:post_id>/',views.post_view, name='post_view')
   
]