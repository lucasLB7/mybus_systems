from django.db import models




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

    reference    = models.CharField(max_length = 3 , blank = True)
    product_name    = models.CharField(max_length = 60 , blank=False)


    def __str__(self):
        return self.product_name
        



 



