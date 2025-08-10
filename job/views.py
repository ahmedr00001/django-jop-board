from django.shortcuts import redirect, render
from .models import Job , Apply , Category
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from .filter import JobFilter
from .form import CategoryForm


# Create your views here.

def job_list(request):
    job_list = Job.objects.all()

    #filters
    filters = JobFilter(request.GET , queryset=job_list)
    job_list = filters.qs

    paginator = Paginator(job_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs' : page_obj  , 'myfilter':filters}
    return render(request , 'job/joblist.html' , context= context)
@login_required
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

@login_required
def add_job (request):
    job_type = Category.objects.all

    if request.method =="POST":
        title = request.POST.get('title')
        jop_type = request.POST.get('jop_type')
        category_name = request.POST.get('category')
        category = Category.objects.get(name=category_name)
        salary = request.POST.get('salary')
        vacancy = request.POST.get('vacancy')
        description = request.POST.get('description')
        experience = request.POST.get('experience')
        image = request.FILES.get('image')

        Job.objects.create(
            title = title,
            jop_type= jop_type,
            description = description,
            vacancy = vacancy,
            salary = salary,
            experience = experience,
            category = category,
            image = image,
            slug = slugify(title),
        )

        return redirect('job:job_list')



    context = {'job_type' : job_type}
    return render(request , 'job/add_Job.html' , context)


def add_category(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect ('job:add_job')


    else:
        category_form = CategoryForm()

    return render(request , 'job/add_category.html', {'category_form':category_form})