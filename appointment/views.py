from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .forms import AppointmentForm, AppointmentCheckForm
from .models import Appointment


def create_appointment(request):
    error = ''
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment:view_checked_appointment')
        else:
            error = "Programarea nu s-a putut realiza"
        
    template_name = 'store/programare.html'
        
    return render(request, template_name, {'form': form, 'error': error})


@ staff_member_required
def view_unchecked_appointment(request):
    unchecked_appointment = Appointment.uncheckedmanager.all()

    return render(request, 'store/programari.html', {'unchecked_app': unchecked_appointment})


def view_checked_appointment(request):
    checked_appointment = Appointment.checkedmanager.all()
    return render(request,'store/programari existente.html', {'checked_app':checked_appointment})
    

def view_detail_appointment(request, slug):
    appointment_detail = get_object_or_404(Appointment, slug=slug)

    form = AppointmentCheckForm(instance=appointment_detail)
    if request.method == 'POST':
        form = AppointmentCheckForm(request.POST, instance=appointment_detail)
        if form.is_valid():
            form.save()

    return render(request, 'store/detalii programare.html', {'appointment_detail': appointment_detail, 'form': form})
