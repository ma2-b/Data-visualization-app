from django.shortcuts import render, redirect

from .models import Product
from .forms import ProductForm
# Create your views here.

def home(request):
    products = Product.objects.all()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("chart:home")
        
    else:
        form = ProductForm()
    
    context = {"products": products, 'form': form}
    return render(request, "chart/home.html", context)


