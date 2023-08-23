#from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from . models import Student
from .forms import StudentForm


def student(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            form = StudentForm()
            return render(request,'index.html',{'form': form})
        
def show(request):
    data = Student.objects.all()
    return render(request,'show.html',{'data': data})


def edit(request,id):
    data = Student.objects.get(id=id)
    return render(request,'edit.html',{'data': data})


def update(request,id):
    data = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=data)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'form':form})


def delete(request,id):
    data = Student.objects.all(id=id)
    data.delete()
    return redirect('/show')