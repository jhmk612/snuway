from django.shortcuts import render, redirect
from .models import Lender
from .forms import LenderForm
from django.contrib.auth.models import User
# Create your views here.

def newlend(request):
    if request.method=='POST':
        f=LenderForm(request.POST)
        if f.is_valid():
            new_lender=f.save(commit=False)
            new_lender.writer=request.user
            new_lender.save()

            return redirect('borrow:lend_view', pk=new_lender.pk)
    else:
        f=LenderForm()

    return render(request, 'lend/lend.html', {'form':f})