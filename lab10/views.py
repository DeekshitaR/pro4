from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Course

def reg(request):
    if request.method == "POST":
        sid = request.POST.get("sname")
        cid = request.POST.get("cname")
        
        try:
            student = Student.objects.get(id=sid)
            course = Course.objects.get(id=cid)
        except Student.DoesNotExist:
            return HttpResponse("<h1>Student does not exist</h1>")
        except Course.DoesNotExist:
            return HttpResponse("<h1>Course does not exist</h1>")
        
        if student.enrolment.filter(id=cid).exists():
            return HttpResponse("<h1>Student already enrolled</h1>")
        
        student.enrolment.add(course)
        return HttpResponse("<h1>Student enrolled successfully</h1>")
    
    else:
        students = Student.objects.all()
        courses = Course.objects.all()
        return render(request, "reg.html", {"students": students, "courses": courses})
