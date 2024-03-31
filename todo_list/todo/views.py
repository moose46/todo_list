from django.shortcuts import render


def home(request):
    print("home(request)")
    return render(request, "home.html")
