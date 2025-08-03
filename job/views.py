from django.shortcuts import render
from .models import Job , Apply
from django.core.paginator import Paginator


# Create your views here.

def job_list(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs' : page_obj }
    return render(request , 'job/joblist.html' , context= context)

def job_detial(request , slug):
    job = Job.objects.get(slug = slug)

    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        cover_letter = request.POST.get('cover_letter')
        cv = request.FILES.get('cv')

        Apply.objects.create(
            job= job,
            name=name,
            email=email,
            website=website,
            cover_letter=cover_letter,
            cv=cv
        )


    context = {'job' : job}
    return render(request , 'job/job_detial.html' , context)