from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTg1fVKRv4HsD3ESQtMcrv5u6ZcM9socXpQrUKSyh_E-NckPTmXF5RL7hg-M364_rehkPg&usqp=CAU")
