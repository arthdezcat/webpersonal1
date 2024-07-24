# pylint: disable=missing-module-docstring
from django.shortcuts import render, HttpResponse
# Create your views here.


def home(request):
    return render(request, "core/home.html")
#def about(request):
 #   return render(request, "core/about.html")
#def discount(request):
 #   return render(request, "core/discount.html")
#def contact(request):
 #   return render(request, "core/contact.html")
#def portfolio(request):
 #   return render(request, "core/portfolio.html")
