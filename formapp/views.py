
# Create your views here.
from django.shortcuts import render

def form_page(request):
    return render(request, 'formapp/form.html')