from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'myapp/index.html')


def allcourse(request):
    return render(request,'myapp/allcourse.html')

def course_detail(request):
    return render(request,'myapp/course_details.html')

def about(request):
    return render(request,'myapp/about.html')