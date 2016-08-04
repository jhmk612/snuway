import re
from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Machine(models.Model):
    name=models.CharField(max_length=40)
    m_type=models.CharField(max_length=30)
    detail=models.ImageField(blank=True)

    def __str__(self):
        return self.name

def price_validator(price):
        if not re.match(r'^\d+$', price):
            raise forms.ValidationError('가격을 제대로 입력해주세요')

class Lender(models.Model):
    machine=models.ForeignKey(Machine)
    latlng=models.CharField(max_length=50)

    price_h=models.CharField(max_length=10, validators=[price_validator], help_text='숫자로만 입력')
    price_d=models.CharField(max_length=10, validators=[price_validator], help_text='숫자로만 입력')
    calendar=models.CharField(max_length=1000)
    writer=models.ForeignKey(User, default=1)

    def lat(self):
        return self.latlng.split(',')[0]
    def lng(self):
        return self.latlng.split(',')[1]


