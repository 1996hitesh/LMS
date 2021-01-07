from django.shortcuts import render
from .models import Courses, Topics, Modules
from users.models import CourseEnrolled
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    userid = request.user.id
    courseEnrolled = CourseEnrolled.objects.filter(user = userid).all()
    
    context = {
        'courses' : courseEnrolled
    }
    for c in courseEnrolled:
        print(c.course.title)
    return render(request, 'index.html', context)

@login_required
def allcourse(request):
    context = {
        'courses' : Courses.objects.all()
    }
    return render(request, 'courses/allcourse.html', context)

@login_required
def course(request, id):
    course = Courses.objects.filter(id=id).first()
    modules = Modules.objects.filter(course_id = course.id).all()
    topics = []
    for module in modules:
        topic = Topics.objects.filter(module_id = module.id).all()
        for t in topic:
            topics.append(t)        
    
    context = {
        'course':course,
        'modules':modules,
        'topics':topics
    }
    return render(request, 'courses/course.html',context)

@login_required
def watch(request, id, tid):
    course = Courses.objects.filter(id=id).first()
    modules = Modules.objects.filter(course_id = course.id).all()
    topics = []
    for module in modules:
        topic = Topics.objects.filter(module_id = module.id).all()
        for t in topic:
            if t.id == tid:
                vid = t
            topics.append(t)
    context = {
        'course': course,
        'modules':modules,
        'topics': topics,
        'vid': vid
    }
    return render(request, 'courses/watch.html',context)
