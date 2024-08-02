from django.shortcuts import render
from django.http import HttpResponse

student_data=[]

# Create your views here.
# def index(request):
# 	return HttpResponse("<h1>Hello world</h1>")
def index(req):
	return render(req,"index.html")
def home(req):
	username=req.GET.get("usrname")
	print(username)
	if(username=="farman"):
		return render(req,"home.html")
	else:
		print("invalid credintial")
def info(req):
	return render(req,"info.html")
def saveInfo(req):
	eno=req.GET.get("eno")
	name=req.GET.get("name")
	marks1=req.GET.get("marks1")
	marks2=req.GET.get("marks2")
	print(eno,name,marks1,marks2)

	student={"eno":eno,
	"name":name,
	"marks1":marks1,
	"marks2":marks2}
	student_data.append(student)
	num_students = len(student_data)
	print(num_students)

	# return HttpResponse("<h1>Hello world</h1>")
	return render(req,"noofstudent.html",{"student":student_data,"number":num_students})

def searchDetail(req):
	eno=req.GET.get("eno")

	found_student=[]
	for student in student_data:
		if student['eno']==eno:
			found_student.append(student) 

	return render(req,"showdetails.html",{"students":found_student})


def showStudentByMarks(req):
	found_student=[]
	for student in student_data:
		if int(student['marks1'])>=70 and int(student['marks2'])>=70:
			found_student.append(student)			
	return render(req,"detailsOfStudentByMarks.html",{"students":found_student})	