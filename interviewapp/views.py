from django.shortcuts import get_object_or_404, render,HttpResponse,redirect,get_list_or_404
from .models import *
# Create your views here.

def home(request):
    questions = Interview_question.objects.all()
    return render(request,'home.html',{"questions":questions})


def add_question(request):
    question = request.POST.get('question',"")
    answer = request.POST.get('answer',"")
    category = request.POST.get('category','')
    flag = False

    if request.method == "POST":
        if question and answer and (category == 'python' or category == 'flask' or category == 'django' or category == 'database'):
            add_question = Interview_question(question = question,
                                          answer = answer , category = category)
            add_question.save()
            return redirect(home)
        else:
            return render(request,'add.html')        

    return render(request,'add.html')

def delete_question(request,id):
    if request.method == "POST":

        question = Interview_question.objects.get(question_number = id)
        # Delete the question
        question.delete()

        return redirect(home)
    return render(request,'home.html')

def python(request):
    python = Interview_question.objects.filter(category = 'python')
    return render(request,'home.html',{'questions':python})

def Django(request):
    Django = Interview_question.objects.filter(category = 'django')
    return render(request,'home.html',{'questions':Django})


def Flask(request):
    Flask = Interview_question.objects.filter(category = 'flask')
    return render(request,'home.html',{'questions':Flask})

def Database(request):
    Database = Interview_question.objects.filter(category = 'database')
    return render(request,'home.html',{'questions':Database})



