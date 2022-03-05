from django.shortcuts import render,redirect
from django.views import View

from .models import*

# Create your views here.
class Index(View):
    def get(self,request):
        contact=Contact.objects.all()
        context={'contact':contact}
        return render(request,'index.html',context)
