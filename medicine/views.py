from django.shortcuts import render,redirect
from .models import Medicine

from .forms import MedForm
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json

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

@require_POST
def update_quantity(request):
    
    data = json.loads(request.body)
    product_id = data.get('product_id')
    action = data.get('action')

    try:
        med = Medicine.objects.get(pk=product_id)
    except Medicine.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

    if action == 'increment':
        med.stock += 1
    elif action == 'decrement' and med.stock > 0:
        med.stock -= 1
    elif action == 'zero':
        med.stock = 0
    elif action == 'delete':
        med.delete()
        return JsonResponse({'success': True})

    med.save()
    return JsonResponse({'stock': med.stock})
