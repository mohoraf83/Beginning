from django.shortcuts import render
def home(req):
    return render(req, "base.html")
def book(req):
    return render(req, "pages/book.html")
def goods(req):
    return render(req,"pages/goods.html")

    

