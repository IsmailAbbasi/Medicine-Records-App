from django.shortcuts import render,redirect
from .models import Medicine

from .forms import MedForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect

def home(request):
    medicine = None
    stock = None
    form = MedForm()

    if request.method == "POST":
        form = MedForm(request.POST, request.FILES)
        if form.is_valid():
            medicine = form.cleaned_data.get("medicine")
            stock = form.cleaned_data.get("stock")

            Medicine.objects.create(medicine=medicine, stock=stock)

            return redirect('home')  
    medicines = Medicine.objects.all().order_by('medicine')

    return render(request, 'medicine/home.html', {
        'form': form,
        'medicines': medicines,
        'stock': stock,
    })
