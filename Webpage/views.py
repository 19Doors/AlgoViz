from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Homepage/index.html")

def contact(request):
    return render(request, "Homepage/contact.html")
