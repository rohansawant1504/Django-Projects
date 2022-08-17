from django.shortcuts import render
from .forms import StudentForm
from .models import students
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

def index(r):
    data = students.objects.all()
    return render(r,'index.html',{'data':data})

def create(r):
    form = StudentForm()
    if r.method =='POST':
        form = StudentForm(r.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
    return render(r,'create.html',{'form':form})

def delete(r,id):
    data = students.objects.get(Roll_No=id)
    data.delete()
    return HttpResponseRedirect('/')

def update(r,id):
    data = students.objects.get(Roll_No=id)
    if r.method=='POST':
        if r.POST['Roll_No'] == str(data.Roll_No):
            form = StudentForm(r.POST,instance=data)
            if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect('/')
        else:
            return HttpResponse('Records not found for given Number')
    return render(r,'update.html', {'data':data})

