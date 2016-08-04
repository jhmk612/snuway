from django import forms
from .models import Lender
from .widgets import DaumMapWidget

class LenderForm(forms.ModelForm):
    class Meta:
        model=Lender
        fields=['machine', 'latlng', 'price_h', 'price_d', 'calendar']
        labels={'machine': '기계종류', 'latlng': '대여위치', 'price_h': '시간당 가격', 'price_d':'일당 가격', 'calendar':'대여가능 날짜'}
        widgets={
            'latlng':DaumMapWidget,
        }