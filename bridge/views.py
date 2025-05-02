from django.shortcuts import render

# Create your views here.
#references to templates only need the file name
#appears that templates must be in a folder named "templates"
def home(request):
    return render(request, "base.html", {})

def nuts(request):
    return render(request, "login.html", {})
