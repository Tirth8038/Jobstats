from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import home_form_hist,home_form_loc,home_form_key,Histogram,Jobs_location
from .utils import *
## Global Spark

@csrf_exempt
def home_view(request):
    context = {}
    context['form1'] = home_form_hist()
    context['form2'] = home_form_loc()
    context['form3'] = home_form_key()
    template_name = "home.html"
    return render(request,template_name,context)


@csrf_exempt
def fetch_data_hist(request):
    if request.POST:
        hist = request.POST['Job_Categories']
        hist = Histogram[int(hist)][1]
        salaries = salary_histogram(hist)
        print(hist,salaries)
        context = {
        "Salaries" : salaries,
        "Category" : hist
        }
        template_name = "hist_plot.html"
        return render(request, template_name, context)

@csrf_exempt
def fetch_data_loc(request):
    if request.POST:
        job_loc = request.POST['Location']
        job_loc = Jobs_location[int(job_loc)][1]

        job_total = get_job_by_category_location(job_loc)
        print(job_loc,job_total)
        context = {
        "Location" : job_loc,
        "Job_count" : job_total
        }
        template_name = "location.html"
        return render(request, template_name, context)


@csrf_exempt
def fetch_data_key(request):
    if request.POST:
        key_word = request.POST['Search_Key']

        total, key_list = get_job_by_category_company(key_word)
        print(total, key_list)
        context = {
        "Total_count" : total,
        "Key_List" : key_list,
        "Keyword" : key_word
        }
        template_name = "key_plot.html"
        return render(request, template_name, context)
