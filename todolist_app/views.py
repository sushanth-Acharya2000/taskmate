from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task_List
from .forms import Task_Form
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def todolist(request):
    if request.method=="POST":
        form=Task_Form(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manager=request.user
            instance.save()
        messages.success(request,("New Task Added!!!"))
        return redirect('todolist')
    else:
        all_task=Task_List.objects.filter(manager=request.user)
        paginator=Paginator(all_task,5)
        page=request.GET.get("pg")
        all_task=paginator.get_page(page)
        return render(request, 'todo.html', {'all_task':all_task})
    
def edit_task(request,task_id):
    if request.method=="POST":
        task_value=Task_List.objects.get(pk=task_id)
        formvalue=Task_Form(request.POST or None,instance=task_value)
        if formvalue.is_valid():
            formvalue.save()
        messages.success(request,("Task successfully edited!!!"))
        return redirect('todolist')
    else:
        task_obj=Task_List.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj':task_obj})
            
def completed_task(request,task_id):
    task=Task_List.objects.get(pk=task_id)
    if(task.manager==request.user):
        task.done=True
        task.save()
    else:
        messages.error(request,("Access Restricated!!!"))
    return redirect('todolist')

def pending_task(request,task_id):
    task=Task_List.objects.get(pk=task_id)
    if(task.manager==request.user):
        task.done=False
        task.save()
    else:
        messages.error(request,("Access Restricated!!!"))
    return redirect('todolist')

 
def delete_task(request,task_id):
    task=Task_List.objects.get(pk=task_id)
    if(task.manager==request.user):
        task.delete()
    else:
        messages.error(request,("Access Restricated!!!"))
    return redirect('todolist')

def index(request):
    index_note={
        'index_note':'Hello!!! welcome to home page'
    }
    return render(request, 'index.html', index_note)

def about(request):
    about={
        'about_note':'Hello!!! welcome about page'
    }
    return render(request, 'about.html', about)


def contact(request):
    contact={
        'contact_note':'Hello!!! welcome to contact us page'
    }
    return render(request, 'contact.html', contact)