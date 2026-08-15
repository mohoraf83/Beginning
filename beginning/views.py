from django.shortcuts import render

def book(request):
    return render(request, "base.html")
def goods(req):
    return render(req,"pages/goods.html")