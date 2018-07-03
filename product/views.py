from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
import datetime as dt


from .models import LaminateFlooring
from .forms import LaminateFlooringForm


def add_laminates(request):
    lam_dict={'LARGO' : 'PLU' , 'CREO' : 'CR' , 'IMPRESSIVE' : 'IM' , 'CLASSIC' : 'CLM' , 'IMPRESSIVE ULTRA' : 'IMU' , 'ELIGNA' : 'EL' , 'ELIGNA WIDE' : 'ELW' , 'LOC FLOOR' : 'LCF'}


    if request.method == 'POST':
        lam_form = LaminateFlooringForm(request.POST)

        if lam_form.is_valid():
            lam           =  lam_form.save(commit=False)
            r             =  lam_form.cleaned_data["rangex"]
            lam.reference =  lam_dict[r]
            lam.save()

            message = "Product added"
        else:
            message = "unsucceful"
    else:
        message = ""


    lam_form  =  LaminateFlooringForm()
    
    return render(request, "products/add-laminates.html" , {"lam_form" : lam_form, 'message':message})
