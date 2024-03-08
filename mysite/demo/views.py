from django.shortcuts import render
from .forms import studentForm
from .models import student,employee
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def forms(request):
    if request.POST:
        form=studentForm(request.POST)
        if form.is_valid:
            form.save()
    form=studentForm()
    return render(request,'forms.html',{'form':form})

def detail(request):
    data=student.objects.all()
    return render(request,'detail.html',{'data':data})



# generic:
# ListView
# DetailView

# CreateView
# UpdateView
# Deleteview
# FormView



class StudentCreateView(CreateView):
    model=student
    fields='__all__'
    success_url='/list/'
    template_name='student_create.html'

class StudentListView(ListView):
    model=student
    template_name='student_list.html'

class StudentUpdateView(UpdateView):
    model=student
    fields='__all__'
    success_url='/list/'
    template_name='student_update.html'

# for employee model create,update,delete,detail

class employeeCreateView(CreateView):
    model=employee
    fields='__all__'
    success_url='/employeelist/'
    template_name='employee_create.html'

class employeeListView(ListView):
    model=employee
    template_name='employee_list.html'

class employeeUpdateView(UpdateView):
    model=employee
    fields='__all__'
    success_url='/employeelist'
    template_name='employee_update.html'

class employeeDeleteView(DeleteView):
    model=employee
    fields='__all__'
    success_url='/employeelist'
    template_name='employee_delete.html'

class employeeDetailView(DetailView):
    model=employee
    template_name='employee_detail.html'