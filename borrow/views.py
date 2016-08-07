from django.shortcuts import render, redirect
from lend.models import Lender
from .models import Comment
from .forms import CommentForm, SearchForm
from lend.forms import LenderForm
# Create your views here.


def lend_list(request):
    lends=Lender.objects.all()
    if request.method=='GET':
        s=SearchForm(request.GET)

        machine=request.GET.get('machine', None)
        if machine:
            lends=lends.filter(machine=machine)

        location=request.GET.get('location', None)
        if location:
            lends=lends.filter(tags=location)

        price=request.GET.get('price', None)
        if price:
            lends=lends.filter(price_h__gte=price)

        date=request.GET.get('date', None)
        if date:
            lends=lends.filter(calendar=date)






    return render(request, 'borrow/index.html', {'lends':lends, 'form':s})





def lend_view(request, pk):
    detail=Lender.objects.get(pk=pk)
    comments=Comment.objects.filter(post=pk)

    if request.method=='POST':
        c=CommentForm(request.POST)
        new_comment=c.save(commit=False)
        new_comment.writer=request.user
        new_comment.post=detail
        new_comment.save()

        return redirect('borrow:lend_view', pk=detail.pk)

    else:
        c=CommentForm()
    context={'detail':detail, 'comments':comments, 'form':c}
    return render(request, 'borrow/lend_view.html', context)

def edit_comment(request, pk, id):
    detail=Lender.objects.get(pk=pk)
    comment=Comment.objects.get(pk=id)

    if request.method=='POST':
        c=CommentForm(request.POST, instance=comment)
        ed_comment=c.save(commit=False)
        ed_comment.writer=request.user
        ed_comment.post=detail
        ed_comment.save()
        return redirect('borrow:lend_view', pk=detail.pk)

    else:
        c=CommentForm(instance=comment)

    context={'detail':detail, 'comment':comment, 'form':c}
    return render(request, 'borrow/edit_comment.html', context)

def delete_comment(request, pk, id):
    detail=Lender.objects.get(pk=pk)
    comment=Comment.objects.get(pk=id)
    comment.delete()
    return redirect('borrow:lend_view', pk=detail.pk)

def lend_edit(request, pk):
    lend=Lender.objects.get(pk=pk)
    if request.method == 'POST':
        l=LenderForm(request.POST, instance=lend)
        ed_lend=l.save(commit=False)
        ed_lend.writer=request.user
        ed_lend.save()
        return redirect('borrow:lendlist')
    else:
        l=LenderForm(instance=lend)

    context={'lend':lend, 'form':l}
    return render(request, 'borrow/edit_lend.html', context)

"""def new_comment(request):
    if request.method=='POST':
        c=CommentForm(request.POST)
        new_comment=f.save(commit=False)
        new_commnent.writer=request.user
        new_comment.save()

        return redirect('/borrow')

    else:
        c=CommentForm()

    return render(request, 'borrow/lend_view.html', {'form':c})"""