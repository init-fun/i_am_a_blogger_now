from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# this is a functional view


def home_view(request, *args, **kwargs):
    context = {}
    return render(request, "home.html", context)


def contact_view(request, *args, **kwargs):
    context = {}
    return render(request, "contact.html", context)


def about_view(request, *args, **kwargs):
    context = {
        "my_txt": "this is a new text",
        "my_num": 234,
        "my_number": [1, 2, 3, 4, 5, 6, 7, 7],
    }
    return render(request, "about.html", context)
