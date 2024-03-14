from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
import datetime

def myView(request):
  all_todos = TodoItem.objects.all()
  return render(request, 'index.html', {
    'all_todos': all_todos
  })

def addTodo(request):
  c = request.POST['content']
  d = request.POST['date_created']

  try:
    d = datetime.datetime.strptime(d, "%Y-%m-%d").date()
  except:
    d = datetime.datetime(2048, 1, 1)

  todo = TodoItem(content=c, date_created=d, is_completed=False)
  todo.save()

  return HttpResponseRedirect('/')

def deleteTodo(request):
  TodoItem.objects.get(id=request.GET['id']).delete()
  return HttpResponseRedirect('/')

def markTodoCompleted(request):
  todo = TodoItem.objects.get(id=request.GET['id'])
  todo.is_completed = True
  todo.save()
  return HttpResponseRedirect('/')

def deleteAllTodo(request):
  for todo in TodoItem.objects.all():
    todo.delete()
  return HttpResponseRedirect('/')
