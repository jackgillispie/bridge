from django.shortcuts import render

# Create your views here.
#references to templates only need the file name
#appears that templates must be in a folder named "templates"
def default(request):
    return render(request, "default.html", {})