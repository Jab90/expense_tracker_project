from . import views
from django.urls import path

urlpatterns = [
path('', views.HomePage.as_view(), name='home'),
path('', views.expense_tool, name='expense_tool'),
path('expense_tool', views.expense_tool, name='expense_tool'),
path('add/', views.add, name='add')
]


