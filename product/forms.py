from django import forms

from .models import LaminateFlooring


# class LaminateFlooringForm(forms.ModelForm):
#     class Meta:
#         model = LaminateFlooring



class LaminateFlooringForm(forms.ModelForm):

    class Meta:
        model    = LaminateFlooring
        exclude  = ('reference' , )
        fields   = '__all__'


# ///////////////////////////////////////////////////////////////


# class SelectFlooringTypeForm(forms.ModelForm):

#     class Meta:
#         model    = 



			