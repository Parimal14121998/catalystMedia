from time import sleep
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UploadFileForm
import csv
from .forms import QueryBuilderForm
from .models import UploadedFile, QueryBody
from .tasks import process_csv


def home(request):
    return render(request, 'home.html')


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            # Process CSV in the background
            process_csv.delay(uploaded_file.file.path)
            messages.success(request, 'File uploaded successfully and is being processed.')
            return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'uploader/upload.html', {'form': form})

def upload_success(request):
    return render(request, 'uploader/success.html')


@login_required
def manage_users(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'New user added')
        else:
            messages.error(request, 'Username already exists')
    users = User.objects.all()
    return render(request, 'uploader/users.html', {'users': users})


@login_required
def query_builder(request):
    form = QueryBuilderForm(request.GET or None)
    results_count = None

    if form.is_valid():
        name = form.cleaned_data.get('name')
        year_founded = form.cleaned_data.get('year_founded')
        industry = form.cleaned_data.get('industry')
        locality = form.cleaned_data.get('locality')
        country = form.cleaned_data.get('country')

        query = QueryBody.objects.all()

        if name:
            query = query.filter(name__icontains=name)
        if year_founded:
            query = query.filter(year_founded=year_founded)
        if industry:
            query = query.filter(industry__icontains=industry)
        if locality:
            query = query.filter(locality__icontains=locality)
        if country:
            query = query.filter(country__icontains=country)

        results_count = query.count()
        messages.success(request, f'{results_count} records found for the query')

    return render(request, 'uploader/query_builder.html', {'form': form, 'results_count': results_count})