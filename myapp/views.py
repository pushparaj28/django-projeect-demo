
# Create your views here.
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello DUNIYA !")


from django.shortcuts import render 

def home(request):
    return render (request,'index.html')