from django.db import models
import datetime as dt




class LaminateFlooring(models.Model):
    PRODUCT_RANGE = (
        ("CREO" , "CREO"),
        ("CLASSIC" , "CLASSIC"),
        ("ELIGNA" , "ELIGNA"),
        ("LARGO" , "LARGO"),
        ("LOC FLOOR" , "LOC FLOOR"),
        ("ELNA WIDE" , "ELIGNA WIDE"),
        ("IMPRESSIVE" , "IMPRESSIVE"),
        ("IMPRESSIVE ULTRA" , "IMPRESSIVE ULTRA"),
    )


    
    rangex = models.CharField(
        max_length = 20,
        choices = PRODUCT_RANGE,
        default = "LARGO"
    )

    reference         = models.CharField(max_length = 3 , blank = True)
    product_name      = models.CharField(max_length = 60 , blank=False)
    date_of_arrival   = models.DateTimeField(auto_now_add=True)
    quantity          = models.PositiveIntegerField(blank = False , null = True)
    purchase_cost     = models.PositiveIntegerField(blank = False , null = True)
    sales_cost        = models.PositiveIntegerField(blank = False , null = True)
    product_picture   = models.ImageField(upload_to='products_directive', null=True, blank=True)


    def __str__(self):
        return self.product_name 

    @classmethod
    def get_by_id(cls, prod_id):
        all_details = LaminateFlooring.objects.filter(pk=prod_id).first()
        return all_details



# //////////////////////////////////////////////////////////////////////////////


class new_laminate_input(models.Model):

    # PRODUCTS = (
    #     ('LAMINATE FLOORING': 'LAMINATE fLOORING' ,'ENIGNEERED WOOD': 'ENIGNEERED WOOD' , 'VINYL FLOORING' : 'VINYL FLOORING'),
    # )

    # select_product_range = models.CharField(max_length = 30 , choices = PRODUCTS, default = "LAMINATE FLOORING" ,  blank = False)

    product_type      = models.OneToOneField(LaminateFlooring , on_delete = models.CASCADE)
    quantity          = models.IntegerField()
    date_of_arrival   = models.DateTimeField()
    ex_works_value    = models.IntegerField()

    def __str__(self):
        return self.product_type
        



 



