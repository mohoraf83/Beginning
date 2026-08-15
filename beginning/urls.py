
from django.contrib import admin
from django.urls import path
from . import views  # از . استفاده کنید چون در same directory هستید

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.book, name='home'),
    path('goods/', views.goods, name='goods'),
]
