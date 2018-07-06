from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
import datetime as dt
import simplejson as json
from django.http import JsonResponse

from .models import LaminateFlooring
from .forms import LaminateFlooringForm
from django.http import HttpResponse, Http404, HttpResponseRedirect


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def add_laminates(request):
    lam_dict={'LARGO' : 'PLU' , 'CREO' : 'CR' , 'IMPRESSIVE' : 'IM' , 'CLASSIC' : 'CLM' , 'IMPRESSIVE ULTRA' : 'IMU' , 'ELIGNA' : 'EL' , 'ELIGNA WIDE' : 'ELW' , 'LOC FLOOR' : 'LCF'}


    if request.method == 'POST':
        lam_form = LaminateFlooringForm(request.POST)

        if lam_form.is_valid():
            lam           =  lam_form.save(commit=False)
            r             =  lam_form.cleaned_data["rangex"]
            lam.reference =  lam_dict[r]
            lam.save()

            message = "Super! Product added"
        else:
            message = "unsucceful"
    else:
        message = ""


    lam_form  =  LaminateFlooringForm()
    
    return render(request, "products/add-laminates.html" , {"lam_form" : lam_form, 'message':message})

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def add_product(request):
    prod_dict = {'LAMINATE FLOOR':'LAMINATE FLOOR' , 'ENIGNEERED WOOD': 'ENIGNEERED WOOD' , 'VINYL FLOORING' : 'VINYL FLOORING'}

    if request.method == "POST":
        pass

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@login_required
def dashboard(request):
    date                          = dt.date.today()
    view_all_laminate_flooring    = LaminateFlooring.objects.all()
    product_count                 = len(LaminateFlooring.objects.all())






    


    return render(request, 'staff/dashboard.html' , {
        "date" : date ,
        "view_all_laminate_flooring" : view_all_laminate_flooring ,
        "product_count"              : product_count ,     
        })


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# def chart_data(request):
#     dataset                       = LaminateFlooring.objects.all() \
#         .values('product_name' ,'quantity' , 'purchase_cost' , 'sales_cost')

#     categories           = list()
#     product_count_series = list()
#     purchase_cost_series = list()
#     sales_cost_series    = list()


#     for entry in dataset:
#         categories.append('%s Class' % entry['product_name'])
#         product_count_series.append(entry['quantity'])
#         purchase_cost_series.append(entry['sales_cost'])   

#         'categories': json.dumps(categories) ,
#         'product_count_series': json.dumps(product_count_series) ,
#         'purchase_cost_series': json.dumps(purchase_cost_series)  })

# return JsonResponse()



def product_details(request):

    date                          = dt.date.today()
    view_all_laminate_flooring    = LaminateFlooring.objects.all()
    # inventory_added_date          = LaminateFlooring.date_of_arrival()
    product_count                 = len(LaminateFlooring.objects.all())








    dataset                       = LaminateFlooring.objects.all() \
        .values('product_name' ,'quantity' , 'purchase_cost' , 'sales_cost')

    categories           = list()
    product_count_series = list()
    purchase_cost_series = list()
    sales_cost_series    = list()
    pie_data=[dict({"name":x.product_name,"y":x.quantity}) for x in view_all_laminate_flooring ]
    print(pie_data)

    for entry in dataset:
        categories.append('%s Class' % entry['product_name'])
        product_count_series.append(entry['quantity'])
        purchase_cost_series.append(entry['purchase_cost'])
        sales_cost_series.append(entry['sales_cost'])   


  

    return render(request, "products/add-new-products-base-query.html" , {
        "date"                           : date ,
        "view_all_laminate_flooring"     : view_all_laminate_flooring ,
        "product_count"                  : product_count ,
        'categories'                     : json.dumps(categories) ,
        'product_count_series'           : json.dumps(product_count_series) ,
        'purchase_cost_series'           : json.dumps(purchase_cost_series) ,
        'sales_cost_series'              : json.dumps(sales_cost_series),
        "entry"                          : view_all_laminate_flooring
        })

  



def product_by_id(request, prod_id):
    title = 'product details'


    # product_details = LaminateFlooring.get_by_id(prod_id)
    product_details = LaminateFlooring.objects.filter(pk=prod_id).first()
    print(product_details)

    return render(request , 'products/product-description.html' , {"title":title , "product_details":product_details})

    


