from django.db import models
from datetime import datetime

# Create your models here.
class Product_master(models.Model):
    product_name = models.CharField(max_length=50,unique=True)
    category_name = models.CharField(max_length=5,default="")
    def __str__(self):
        return self.product_name + " " + self.category_name
    
class Waste_item_master_list(models.Model):
    waste_item_code = models.CharField(max_length=9,unique=True)
    description_EN = models.CharField(max_length=50,default="")
    description_TH = models.CharField(max_length=100,default="")
    waste_group_code = models.CharField(max_length=5,default="")
    waste_unit = models.CharField(max_length=5,default="")
    systems_date = models.DateField(default=datetime.now)
    update_date = models.CharField(max_length=20,default="")
    update_by = models.CharField(max_length=100,default="")

class Waste_group_master_list(models.Model):
    waste_group_code = models.CharField(max_length=5,unique=True)
    group_name = models.CharField(max_length=100,default="")
    systems_date = models.DateField(default=datetime.now)
    update_date = models.CharField(max_length=20,default="")
    update_by = models.CharField(max_length=100,default="")

class Waste_item_price_list(models.Model):
    waste_item_code = models.CharField(max_length=9,unique=True)
    price = models.FloatField(default=0.0)
    unit_price	 = models.CharField(max_length=5,default="")	
    price_effective_from = models.CharField(max_length=20,default="")
    price_effective_to = models.CharField(max_length=20,default="")
    date_code_from = models.IntegerField(default=0)
    date_code_to = models.IntegerField(default=0)
    company_code = models.CharField(max_length=10,default="")
    systems_date = models.DateField(default=datetime.now)
    update_date = models.CharField(max_length=20,default="")
    update_by = models.CharField(max_length=100,default="")

class Company_master_list(models.Model):
    company_code = models.CharField(max_length=10,unique=True)
    company_name = models.CharField(max_length=100,default="")
    systems_date = models.DateField(default=datetime.now)
    update_date = models.CharField(max_length=20,default="")
    update_by = models.CharField(max_length=100,default="")

class Company_contact_name_list(models.Model):
    company_code = models.CharField(max_length=10)
    contact_firstname = models.CharField(max_length=100,default="")
    contact_lastname = models.CharField(max_length=100,default="")
    contact_email = models.CharField(max_length=50,default="")
    contact_phone = models.CharField(max_length=20,default="")
    systems_date = models.DateField(default=datetime.now)
    update_date = models.CharField(max_length=20,default="")
    update_by = models.CharField(max_length=100,default="")

class Waste_item_map_factory(models.Model):
    waste_item_code = models.CharField(max_length=9)
    factory_name = models.CharField(max_length=5)
    systems_date = models.DateField(default=datetime.now)
    update_date = models.CharField(max_length=20,default="")
    update_by = models.CharField(max_length=100,default="")

class Waste_daily_transaction(models.Model):
    date_take_off = models.CharField(max_length=20,default="")
    factory_name = models.CharField(max_length=5,default="")
    waste_item_code = models.CharField(max_length=9,default="")
    waste_group_code = models.CharField(max_length=5,default="")
    detail_no = models.CharField(max_length=20,default="")
    weight = models.CharField(max_length=20,default="")
    systems_date = models.DateField(default=datetime.now)
    update_date = models.CharField(max_length=20,default="")
    update_by = models.CharField(max_length=100,default="")





