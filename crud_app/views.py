from django.shortcuts import render,redirect
from .models import*
# Create your views here.




def Create(request):
  if request.POST:
      name= request.POST["name"]
      phone = request.POST["phone"]
      email= request.POST["email"]
      address = request.POST["address"]

      Employee.objects.create(name=name,phone=phone,email=email,address=address)
      return redirect("read")
  else:
     return render(request,"crud.html")


def read(request):
    uid = Employee.objects.all()  
    con = {"uid":uid}
    return render(request,"crud.html",con)


def update(request,id):
  uid = Employee.objects.get(id=id)
  if request.POST:
      name= request.POST["name"]
      phone = request.POST["phone"]
      email= request.POST["email"]
      address = request.POST["address"]

      uid.name=name
      uid.phone=phone
      uid.email=email
      uid.address=address

      uid.save()
      
      return redirect("read")
  else:
     return render(request,"crud.html")



def delete(request,id):
     uid = Employee.objects.get(id=id)
     uid.delete()
     return redirect("read")
 
     