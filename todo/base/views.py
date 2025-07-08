from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse

# Create your views here.



def works(request):
    return HttpResponse("works")