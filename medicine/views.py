from django.shortcuts import render,redirect
from .models import Medicine
from django.contrib.auth.decorators import login_required
from .forms import MedForm
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.contrib.auth import get_user_model

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('account_login')

@login_required
@csrf_protect
def dashboard(request):
    medicine = None
    stock = None
    form = MedForm()

    if request.method == "POST":
        form = MedForm(request.POST, request.FILES)
        if form.is_valid():
            medicine = form.cleaned_data.get("medicine")
            stock = form.cleaned_data.get("stock")

            Medicine.objects.create(
                user = request.user,
                medicine=medicine,
                stock=stock
            )

            return redirect('dashboard')
        
    medicines = Medicine.objects.filter(user=request.user).order_by('medicine')

    return render(request, 'medicine/home.html', {
        'form': form,
        'medicines': medicines,
        'stock': stock,
    })

@require_POST
@login_required
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

def activation_cron(request):
    User = get_user_model()
    user_count = User.objects.count()
    return HttpResponse(f"Total users: {user_count}")