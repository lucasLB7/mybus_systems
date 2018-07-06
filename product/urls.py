from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


from . import views



app_name = "product"

urlpatterns = [
    url(r'^product/laminate_flooring$' , views.add_laminates, name = "newlaminates"),
    url(r'^$', views.dashboard , name = 'dashboard'),
    url(r'^product/product_details$' , views.product_details , name = "proddetails"),
    url(r'^product/product_by_id/(?P<prod_id>\d+)$' , views.product_by_id , name = 'prodid')
    
]