from django.shortcuts import render, redirect
from .forms import UserContactForm
from .models import Contact


# Create your views here.
def contact(request):
    if(request.method == 'POST'):

        form = UserContactForm(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('contact')

    else:
        form = UserContactForm()
    contct = Contact.objects.all()[::-1]
    return render(request,'contact.html',{'form':form,'contct':contct})


def admin_home(request):


    contact = Contact.objects.all()[::-1]
    for i in contact:
        i.status = 1
        i.save()
    return render(request,'admin_home.html',{'contact':contact})
