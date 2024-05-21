from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from  django.core.mail import send_mail
# Create your views here.

def register(request):
    EUFO = UserForm()
    EPFO = ProfileForm()
    d = {'EUFO': EUFO, 'EPFO':EPFO}
    if request.method == 'POST' and request.FILES:
        UFDO = UserForm(request.POST)
        PFDO = ProfileForm(request.POST, request.FILES)
        if UFDO.is_valid() and PFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = PFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            message=f"Hello{UFDO.cleaned_data.get('first_name')} your registration is done successfully \n\n thankx regards Team...❤"
            email=UFDO.cleaned_data.get('email')
            send_mail(
                'Registration successfull',
                      message,
                      'mamasahoo43442@gmail.com',
                      [email],
                      fail_silently=False
                      )
            return HttpResponse('registration is Done')
        return HttpResponse('Invalid Data')
    return render(request, 'register.html', d)