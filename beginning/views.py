from django.shortcuts import render

def book(req):
    return render(req, "pages/book.html")
def home(req):
    return render(req, "base.html")
def goods(req):
    return render(req,"pages/goods.html")

    

