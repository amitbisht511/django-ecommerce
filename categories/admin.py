from django.contrib import admin
from .models import Category

# Register your models here.
@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
  def products_count(self, obj):
    return obj.category_products.count()
  products_count.short_description = 'Products Count'
  list_display = ('title', 'slug', 'products_count', 'description')
  list_filter = ('status',)
  ordering = ('title', 'slug', 'description')
