from django.db import models

from django.template.defaultfilters import slugify

class Appointment(models.Model):
    
    class VerifiedAppointmentManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(checked=True)
        
    class UnVerifiedAppointmentManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(checked=False)
        
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    slug = models.SlugField(unique=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    
    DAY = [
        ('Lun', 'Luni'),
        ('Mar', 'Marti '),
        ('Mie', 'Miercuri'),
        ('Joi', 'Joi'),
        ('Vin', 'Vineri'),
        ('Sam', 'Sambata'),
        ('Dum', 'Duminica'),
    ]
    
    day = models.CharField(max_length=100, choices=DAY, default=None)
    
    APPOINTMENT = [
        ('PR1', '12:00-13:00'),
        ('PR2', '13:00-14:00'),
        ('PR3', '14:00-15:00'),
        ('PR4', '15:00-16:00'),
        ('PR5', '16:00-17:00'),
        ('PR6', '17:00-18:00'),
    ]
    
    appointment = models.CharField(max_length=100, choices=APPOINTMENT, default=None)
    
    FRIZER = [
        ('FR1', 'Claudiu'),
        ('FR2', 'Ivanciu'),
        ('FR3', 'Gheorghe'),
    ]
    
    frizer = models.CharField(max_length=100, choices=FRIZER, default=None)
    
    PACHET = [
        ('PAC1', 'Tuns'),
        ('PAC2', 'Tuns + Barba'),
        ('PAC3', 'Tuns + Barba + Aranjat'),
        ('PAC4', 'Barba'),
        ('PAC5', 'Vopsit barba'),
        ('PAC6', 'Pensat'),
    ]
    
    pachet = models.CharField(max_length=100, choices=PACHET, default=None)
    checked = models.BooleanField(default=False)
    
    class Status(models.TextChoices):
        STAT1 = 'stat1', 'In asteptare'
        STAT2 = 'stat2', 'Acceptat'
        STAT3 = 'stat3', 'Refuzat'

    
    status = models.CharField(max_length=40, choices=Status.choices, default=Status.STAT1)
    
    objects = models.Manager()
    checkedmanager = VerifiedAppointmentManager()
    uncheckedmanager = UnVerifiedAppointmentManager()
    
    def get_absolute_url(self):
        return reverse('appointment:view_detail_appointment', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.created)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name