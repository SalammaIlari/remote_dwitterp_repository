from django.shortcuts import render
from .models import Account
from .forms import AccountForm
def home(request):
    return render(request,'home.html')
def account_view(request):
    if request.method=="POST":
        cform=AccountForm(request.POST)
        if cform.is_valid():
            name=cform.cleaned_data.get('name','')
            email=cform.cleaned_data.get('email', '')
            contact_no=cform.cleaned_data.get('contact_no','')
            describe_yourself=cform.cleaned_data.get('describe_yourself','')
            what_are_you_in_interested=cform.cleaned_data.get(' what_are_you_in_interested','')
            Preferred_Languages=cform.cleaned_data.get('Preferred_Languages', '')
            data=Account(
                name=name,
                email= email,
                contact_no=contact_no,
                describe_yourself=describe_yourself,
                what_are_you_in_interested=what_are_you_in_interested,
                Preferred_Languages=Preferred_Languages
            )
            data.save()
            cform=AccountForm()
            return render(request,'account.html',{'cform':cform})
    else:
        cform =AccountForm()
        return render(request,'account.html',{'cform': cform})
def test2_view(request):
    return render(request,'test2.html')
def test3_view(request):
    return render(request,'test3.html')
def test4_view(request):
    return render(request,'test4.html')


