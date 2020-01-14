from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=40) 					   #Наименование товара
    description = models.CharField(max_length=200, default="") #Описание товара
    price = models.IntegerField()			  				   #Цена товара
    quantity = models.IntegerField(default=0) 				   #Количество товара на складе
    def __str__(self):
    	return (f"{self.id}: {self.name}")