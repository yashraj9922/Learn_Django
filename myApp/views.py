from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    context = {"variable1": "this is sent", "variable2": "with Yashraj"}
    return render(request, "index.html")
    # return HttpResponse("This is HomePage of myApp")


def about(request):
    # return HttpResponse("This is AboutPage of myApp")
    return render(request, "about.html")


def services(request):
    # return HttpResponse("This is ServicesPage of myApp")
    return render(request, "services.html")


def contacts(request):
    # return HttpResponse("This is ContactPage of myApp")
    return render(request, "contact.html")
