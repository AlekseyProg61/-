from django.contrib import admin
from .models import Category,Product
# Register your models here.
@ admin.register(Category) 
class Showcase(admin.ModelAdmin):
    list_display = ['name','description']
    list_filter = ['name']

@ admin.register(Product) 
class Showcase(admin.ModelAdmin):
    list_display = ['name_product','description','image_product','avialable',
                    'price','date_create'
                    ]
    list_filter = ['name_product']