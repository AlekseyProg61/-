
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    phone = models.IntegerField(verbose_name="Телефон",null=True,blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', verbose_name="Фото",height_field=150, width_field=250, max_length=None,blank=True,null=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения",blank=True,null =True)
