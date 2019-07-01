from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEDIUMS = (
    ('L', 'Lavender'),
    ('E', 'Earth'),
    ('W', 'Water'),
    ('M', 'Moonlight')
)

class Lore(models.Model):
  lore = models.TextField(max_length=500)
  
  def __str__(self):
    return self.lore

  def get_absolute_url(self):
    return reverse('lores_detail', kwargs={'pk': self.id})

class Crystal(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  mining = models.TextField(max_length=250)
  uses = models.TextField(max_length=500) 
  lores = models.ManyToManyField(Lore)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  
  def __str__(self):
    return self.lore

  def get_absolute_url(self):
    return reverse('detail', kwargs={'crystal_id': self.id})

  

class Charging(models.Model):
  date = models.DateField('charging date')
  medium = models.CharField(
    max_length=1,
    choices=MEDIUMS,
    default=MEDIUMS[0][0]
  )
  crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_medium_display()} on {self.date}"

  class Meta:
    ordering = ['-date']