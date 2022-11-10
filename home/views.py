from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
     #return HttpResponse(" this is my home page(/)")
     context = { 'name': 'Bruce', 'course':'Astronomy' }
     return render(request, 'home.html', context)

def about(request):
     #return HttpResponse(" this is my about page(/about)")
     return render(request, 'about.html')

def projects(request):
     #return HttpResponse(" this is my project page(/projects)")
     return render(request, 'projects.html')

def contact(request):
     if request.method ==  'POST':
          name = request.POST['name']
          email = request.POST['email']
          phone = request.POST['phone']
          desc = request.POST['desc']
          #print(name, email, phone, desc)
          ins = Contact(name=name, email=email, phone=phone, desc=desc)
          ins.save()
          print("The data has written to the database")
     #eturn HttpResponse(" this is my contact page(/contact)")
     return render(request, 'contact.html')


   