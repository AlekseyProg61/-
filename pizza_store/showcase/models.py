from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="Категория",max_length=100)
    description = models.TextField(verbose_name='Описание',max_length=1000,blank=True)
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return f'{self.name}'
    
class Product(models.Model):
    category = models.ForeignKey(Category,verbose_name="Категория",on_delete=models.CASCADE)
    name_product = models.CharField(verbose_name="Название продукта",max_length=200)
    description = models.TextField(verbose_name="Описание",max_length=1000,blank=True,null=True)
    image_product = models.ImageField(upload_to='',verbose_name="Изображение товара")
    avialable = models.BooleanField(verbose_name="Доступен",default=True)
    price = models.DecimalField(verbose_name="Цена",decimal_places=2,max_digits=7)
    date_create = models.DateTimeField(verbose_name="Дата создания",auto_now=True)
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    def __str__(self):
        return f'Категория {self.category}, Название {self.name_product}, Цена {self.price}'