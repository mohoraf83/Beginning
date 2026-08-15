from django.shortcuts import render


def book(req):
    return render(req, "base.html")
