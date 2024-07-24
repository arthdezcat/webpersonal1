from django.shortcuts import render
from .models import Catalago, Sucursales, Contactos, Discounts

def about(request):
    projectCatalago = Catalago.objects.all()  
    return render(request, "front/about.html",{'projectCatalago':projectCatalago})
def portfolio(request):
    projectSucursales = Sucursales.objects.all()  
    return render(request, "front/portfolio.html",{'projectSucursales':projectSucursales})
def contact(request):
    projectContactos = Contactos.objects.all()  
    return render(request, "front/contact.html",{'projectContactos':projectContactos})
def discount(request):
    projectDiscounts = Discounts.objects.all()  
    return render(request, "front/discount.html",{'projectDiscounts':projectDiscounts})