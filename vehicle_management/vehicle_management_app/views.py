from django.shortcuts import render,redirect
from django.http import HttpResponse 
from vehicle_management_app.models import record

# Create your views here.
def vehicle_info(request):
    if request.method=="POST":
        n=request.POST['vehicle_number']
        t=request.POST['v_type']
        mod=request.POST['model']
        des=request.POST['des']
        
        p=record.objects.create(num=n, vehicletype=t, vehiclemodel=mod, vehicledes=des)
        p.save() 
        return redirect('/read')

    else:
        return render(request,'vehicle_info.html')
    

def index(request):
    return render(request,'index.html')

def readdata(request):
    p=record.objects.all()
    content={}
    content['data']=p
    return render(request,'readdata.html',content) 

def edit(request,rid):
    if request.method=="POST":
        un=request.POST['vehicle_number']
        ut=request.POST['v_type']
        umod=request.POST['model']
        udes=request.POST['des']

        p=record.objects.filter(id=rid)
        p.update(num=un, vehicletype=ut, vehiclemodel=umod, vehicledes=udes)
        return redirect('/read')
    else:

        p=record.objects.filter(id=rid)
        content={}
        content['data']=p
        return render(request,'edit.html',content)

def delete(request,rid):
    p=record.objects.get(id=rid)
    p.delete()
    return redirect('/read')