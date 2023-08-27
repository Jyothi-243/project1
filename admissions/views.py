from django.shortcuts import render
from admissions.models import Student
from admissions.forms import StudentModelForm
from admissions.forms import VendorForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# views are of 2 types 1.functional based views 2.class based views
#  function based view
@login_required
def homepage(request):
    return render(request,'index.html')
def logoutUser(request):
    return render(request,'logout.html')


@login_required
def addAdmissions(request):
    form=StudentModelForm
    Studentform={'form':form}
    if request.method =='POST':
        form =StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)
    return render(request,'Admissions/addAdmissions.html',Studentform);
@login_required
def admissionsReport(request):
    result = Student.objects.all();
    students = {"allstudents": result}
    return render(request,'Admissions/admissionsReport.html',students);

@login_required
def deleteStudent(request,id):
    s=Student.objects.get(id=id)  #select *from admissions_student where id=idvalue
    s.delete()
    return admissionsReport(request)
@login_required
def updateStudent(request,id):
    s=Student.objects.get(id=id)
    form=StudentModelForm(instance=s)
    dict={'form':form}
    if request.method=='POST':
        form=StudentModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return admissionsReport(request)
    return render(request,'admissions/update-admissions.html',dict)
@login_required
def addVendor(request):
    form=VendorForm
    vform={'form':form}
    if request.method =='POST':
        form =VendorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['address'])
            print(form.cleaned_data['contact'])
            print(form.cleaned_data['item'])
        return homepage(request)
    return render(request,'Admissions/add-vendor.html',vform);
