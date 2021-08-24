from django.db import models

from django.template.defaultfilters import slugify
import uuid

class Appointment(models.Model):
    
    class VerifiedAppointmentManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(checked=True)
        
    class UnVerifiedAppointmentManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(checked=False)
        
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    slug = models.SlugField(max_length=200, null=False, unique=True, blank=True)
    
    # created = models.DateTimeField(auto_now_add=True)
    
    class Day(models.TextChoices):
        ZI1 = 'Luni', 'Luni'
        ZI2 = 'Marti', 'Marti'
        ZI3 = 'Miercuri', 'Miercuri'
        ZI4 = 'Joi', 'Joi'
        ZI5 = 'Vineri', 'Vineri'
        ZI6 = 'Sambata', 'Sambata'
        ZI7 = 'Duminica', 'Duminica'
    
    
    day = models.CharField(max_length=100, choices=Day.choices, default=Day.ZI1)
    
    class Appointment(models.TextChoices):
        ORA1 = '12:00-13:00', '12:00-13:00'
        ORA2 = '13:00-14:00', '13:00-14:00'
        ORA3 = '14:00-15:00', '14:00-15:00'
        ORA4 = '15:00-16:00', '15:00-16:00'
        ORA5 = '16:00-17:00', '16:00-17:00'
        ORA6 = '17:00-18:00', '17:00-18:00'
    
    appointment = models.CharField(max_length=100, choices=Appointment.choices, default=Appointment.ORA1)
    
    class Frizer(models.TextChoices):
        STAT1 = 'Claudiu', 'Claudiu'
        STAT2 = 'Ivanciu', 'Ivanciu'
        STAT3 = 'Gheorghe', 'Gheorghe'
    
    frizer = models.CharField(max_length=100, choices=Frizer.choices, default=Frizer.STAT1)
    
    class Pachet(models.TextChoices):
        PC1 = 'tuns', 'Tuns'
        PC2 = 'tuns_barba', 'Tuns + Barba'
        PC3 = 'tuns_barba_aranjat', 'Tuns + Barba + Aranjat'
        PC4 = 'babra', 'Barba'
        PC5 = 'vopsit_barba', 'Vopsit barba'
        PC6 = 'pensat', 'Pensat'
    
    pachet = models.CharField(max_length=100, choices=Pachet.choices, default=Pachet.PC1)
    checked = models.BooleanField(default=False)
    
    class Status(models.TextChoices):
        STAT1 = 'In asteptare', 'In asteptare'
        STAT2 = 'Acceptat', 'Acceptat'
        STAT3 = 'Refuzat', 'Refuzat'

    
    status = models.CharField(max_length=40, choices=Status.choices, default=Status.STAT1)
    
    objects = models.Manager()
    checkedmanager = VerifiedAppointmentManager()
    uncheckedmanager = UnVerifiedAppointmentManager()
    
    def get_absolute_url(self):
        return reverse('appointment:view_detail_appointment', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
