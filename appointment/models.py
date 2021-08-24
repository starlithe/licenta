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
    slug = models.SlugField(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    
    DAY = [
        ('Luni', 'Luni'),
        ('Marti', 'Marti '),
        ('Miercuri', 'Miercuri'),
        ('Joi', 'Joi'),
        ('Vineri', 'Vineri'),
        ('Sambata', 'Sambata'),
        ('Duminica', 'Duminica'),
    ]
    
    day = models.CharField(max_length=100, choices=DAY, default=None)
    
    APPOINTMENT = [
        ('12:00-13:00', '12:00-13:00'),
        ('13:00-14:00', '13:00-14:00'),
        ('14:00-15:00', '14:00-15:00'),
        ('15:00-16:00', '15:00-16:00'),
        ('16:00-17:00', '16:00-17:00'),
        ('17:00-18:00', '17:00-18:00'),
    ]
    
    appointment = models.CharField(max_length=100, choices=APPOINTMENT, default=None)
    
    FRIZER = [
        ('Claudiu', 'Claudiu'),
        ('Ivanciu', 'Ivanciu'),
        ('Gheorghe', 'Gheorghe'),
    ]
    
    frizer = models.CharField(max_length=100, choices=FRIZER, default=None)
    
    PACHET = [
        ('Tuns', 'Tuns'),
        ('Tuns + Barba', 'Tuns + Barba'),
        ('Tuns + Barba + Aranjat', 'Tuns + Barba + Aranjat'),
        ('Barba', 'Barba'),
        ('Vopsit barba', 'Vopsit barba'),
        ('Pensat', 'Pensat'),
    ]
    
    pachet = models.CharField(max_length=100, choices=PACHET, default=None)
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
