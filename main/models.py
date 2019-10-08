from django.db import models

from localflavor.us.us_states import US_STATES


class Company(models.Model):
    name = models.CharField(max_length=128, )
    phone = models.CharField(max_length=16, null=True, blank=True, verbose_name='Phone')
    email = models.EmailField(null=True, blank=True, )
    state = models.CharField(choices=US_STATES, blank=True, null=True, max_length=2)
    
    class Meta:
        ordering = ['-id']
        verbose_name = "Company"
        verbose_name_plural = "Companies"
    
    def __str__(self):
        return self.name
