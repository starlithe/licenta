from django.shortcuts import render, get_object_or_404

from .forms import AppointmentForm, AppointmentCheckForm
from .models import Appointment

def create_appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm()
        if form.is_valid():
            form.save()
        
    template_name = ''
        
    return render(request, template_name, {'form': form})


def view_unchecked_appointment(request):
    unchecked_appointment = Appointment.uncheckedmanager.all()
    return render(request, {'unchecked_app':unchecked_appointment})


def view_checked_appointment(request):
    checked_appointment = Appointment.checkedmanager.all()
    return render(request, {'checked_app':checked_appointment})
    
def view_detail_appointment(request, slug):
    appointment_detail = get_object_or_404(Appointment, slug=slug)
    
    form = AppointmentCheckForm(instance=appointment_detail)
    if request.method == 'POST':
        form = AppointmentCheckForm(request.POST, instance=appointment_detail)
        if form.is_valid():
            form.save()
            
    return render(request, 'store/detalii programare.html', {'appointment_detail':appointment_detail, 'form':form})