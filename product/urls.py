from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


from . import views



app_name = "product"

urlpatterns = [
    url(r'^product/laminate_flooring$' , views.add_laminates, name = "newlaminates"),
]