from .models import Course
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from django import template
from django.shortcuts import render


@login_required(login_url="/login/")
def courses_view(request):
    context = {
        'courses': Course.objects.all(),
        'segment': 'courses'
    }
    return render(request, 'courses/courses-list.html', context)
