"""from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello")
def add(request):
    return render(request, 'add.html')
    #return HttpResponse("Enter event details")
def display(request):
    return HttpResponse("display event details")
def Update(request):
    return HttpResponse("Update event details")"""""

from django.http import HttpResponse
from django.shortcuts import render
from .models import event_scheduler
from django.forms import ModelForm

class Updatedata(ModelForm):
    class Meta:
        model=event_scheduler
        fields='__all__'
                
def index(request):
    return render(request, 'index.html')

def add(request):
    x = event_scheduler.objects.all()
    if request.method == 'POST':
        i=request.POST['quantity']
        name = request.POST['eventname']
        date = request.POST['birthday']
        time = request.POST['appt']
        description = request.POST['message']

        new_event = event_scheduler(i=i,name=name, date=date, time=time, description=description)
        new_event.save()
        return HttpResponse("Data Saved")
    return render(request, 'add.html')

def display(request):
    if request.method == 'POST':
        i=request.POST['quantity']
        name = request.POST['eventname']
        date = request.POST['birthday']
        time = request.POST['appt']
        description = request.POST['message']
        obj=event_scheduler(i=i)
        obj.i=i
        obj.name=name
        obj.date=date
        obj.time=time
        obj.description=description
        obj.save()
    from django.core import serializers
    data = serializers.serialize("python",event_scheduler.objects.all())
    context = {
        'data': data,
    }
    return render(request, 'display.html',context)

def display_filter(request):
    if request.method == 'POST':
        event_id = request.POST.get('quantity')
        events = event_scheduler.objects.filter(i=event_id)
        return render(request, 'display_filter.html', {'events': events})
    return render(request, 'input.html')

def delete(request):
    if request.method == 'POST':
        event_id = request.POST.get('id')
        events = event_scheduler.objects.filter(i=event_id)
        if events.exists():
            events.delete()
            return HttpResponse("Data deleted")
        else:
            return HttpResponse("Data Not found")
    return render(request, 'delete.html')

def update(request):
    if request.method == 'POST':
        event_id = request.POST.get('quantity')
        events = event_scheduler.objects.filter(i=event_id)
        if events.i==event_id:
            i = request.POST['quantity']
            name = request.POST['eventname']
            date = request.POST['birthday']
            time = request.POST['appt']
            description = request.POST['message']
            events.save()            
            return HttpResponse("Data Updated")
           #return render(request, 'update.html', {'events': events})
        else:
            return HttpResponse("Data Not found")
    return render(request, 'update.html')






