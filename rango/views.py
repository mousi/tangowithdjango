from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!<br /><a href=\"about/\">About</a>")
def about(request):
    return HttpResponse("Rango says here is the about page.<br /><a href=\"../\">Index</a>")