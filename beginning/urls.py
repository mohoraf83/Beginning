
from django.contrib import admin
from django.urls import path
from . import views  # از . استفاده کنید چون در same directory هستید

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.home,),
    path('book/',  views.book, name='book'),
    path('goods/', views.goods, name='goods'),
]
