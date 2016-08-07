from django import forms
from .models import Lender, Tag
from .widgets import DaumMapWidget

class LenderForm(forms.ModelForm):
    class Meta:
        model=Lender
        fields=['machine', 'latlng', 'price_h',  'calendar', 'tags']
        labels={'machine': '기계종류', 'latlng': '대여위치', 'price_h': '가격',  'calendar':'대여가능 날짜', 'tags': '태그'}
        widgets={
            'latlng':DaumMapWidget,
        }