from django.shortcuts import render,redirect
from django.views import View

from .forms import *
from .models import *

# Create your views here.
class Index(View):
    def get(self,request):
        contact=Contact.objects.all()
        context={'contact':contact}
        return render(request,'index.html',context)

class AddContact(View):
    def get(self,request):
        form=AddContactForm()
        context={'form':form}
        return render(request,'add.html',context)

    def post(self,request):
        form=AddContactForm(request.POST)            
        if form.is_valid():
            form.save()
        return redirect('index')    

