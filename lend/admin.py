from django.contrib import admin
from .models import Lender, Machine, Tag
from .forms import LenderForm
# Register your models here.
class LenderAdmin(admin.ModelAdmin):
    form=LenderForm



admin.site.register(Lender, LenderAdmin)
admin.site.register(Machine)
admin.site.register(Tag)
