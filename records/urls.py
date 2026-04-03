from django.urls import path
from .views import *

urlpatterns = [
    path('', list_records),
    path('create/', create_record),
    path('update/<int:pk>/', update_record),
    path('delete/<int:pk>/', delete_record),
]