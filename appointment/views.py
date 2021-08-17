from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .forms import AppointmentForm
from .models import Appointment

def create_appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm()
        if form.is_valid():
            form.save()
        
    template_name = ''
        
    return render(request, template_name, {'form': form})


@ staff_member_required
def view_unchecked_appointment(request):
    unchecked_appointment = Appointment.uncheckedmanager.all()

    return render(request, 'store/programari.html', {'unchecked_app': unchecked_appointment})


def view_checked_appointment(request):
    checked_appointment = Appointment.checkedmanager.all()
    return render(request,'store/programari existente.html', {'checked_app':checked_appointment})
    
def view_detail_appointment(request, slug):
    appointment_detail = get_object_or_404(Appointment, slug=slug)
    return render(request, {'appointment_detail':appointment_detail})
