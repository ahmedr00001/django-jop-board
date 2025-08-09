from django.shortcuts import render
from django.db.models import Count
from job.models import Job , Category
# Create your views here.


def homepage (request):
    categories = Category.objects.annotate(job_count=Count('job'))
    job_number = Job.objects.count()
    numbers = range(1,9)
    context = {'categories': categories,'job_number':job_number, 'numbers':numbers}
    return render(request , 'index.html' , context)