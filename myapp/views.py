from django.shortcuts import render,redirect
from .models import StudentModel

def Create_Student(req):
    if req.method == "POST":
        name = req.POST.get('name')
        dob = req.POST.get('dob')
        email = req.POST.get('email')
        
        StudentModel.objects.create(
            name = name,
            dob = dob,
            email = email,
        )
        return redirect('Student_List')
    return render(req,'createstudent.html')

def Student_List(req):
        student_data = StudentModel.objects.all()
        
        context ={
            'student':student_data
        }
        return render(req,'studentlist.html',context)
    
def Edit_Student(req,id):
    student = StudentModel.objects.get(id=id)
    if req.method == "POST":
        student.name = req.POST.get('name') 
        student.dob = req.POST.get('dob') 
        student.email = req.POST.get('email')
        student.save()
    
        return redirect('Student_List')
    return render(req,'edit.html',{'Student':student})

def Delete_Student(req,id):
    student = StudentModel.objects.get(id=id)
    student.delete()
    return redirect('Student_List')

def Home(req):
    return render(req,'home.html')