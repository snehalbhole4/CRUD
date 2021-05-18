from django.shortcuts import render,redirect
from .forms import EmployeeForm
from . models import Employee



# Create your views here



def retrieve_view(request):
    employee = Employee.objects.all()
    context = {'employee': employee}
    return render(request,'Newapp/first.html',context)



def createview(request):
    form = EmployeeForm()
    context = {'form': form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
 #       return redirect('Newapp/first.html')
    return render(request, 'Newapp/create.html', context)

def update_view(request,id):
    employ = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employ)
        if form.is_valid():
            form.save()
        return redirect('/na/upd/')
    return render(request,'Newapp/update.html',{'employ': employ})


def delete_view(request,id):
    e = Employee.objects.get(id=id)
    e.delete()
    return redirect('/na/del/')

def del_view(request):
    return render(request,'Newapp/delete.html')

def update_success(request):
    return render(request,'Newapp/update_success.html')


