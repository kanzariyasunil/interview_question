from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='home'),
    path('add_question', add_question,name='add_question'),
    path('delete/<int:id>',delete_question,name='delete_question'),
    path('python',python,name = 'python'),
    path('django',Django,name='Django'),
    path('flask',Flask,name='flask'),
    path('database',Database,name='database')

]