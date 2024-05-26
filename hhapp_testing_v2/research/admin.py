from django.contrib import admin

# Register your models here.
from .models import Category, Refrigerator, Compressor, ResearchRef

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Refrigerator)
class RefrigeratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount_compressor', 'no_frost', 'category')
    list_filter = ('name', 'amount_compressor', 'no_frost', 'category')
    search_fields = ('name', 'amount_compressor', 'no_frost', 'category')


@admin.register(Compressor)
class CompressorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', 'refrigerator')
    search_fields = ('name', 'refrigerator')


@admin.register(ResearchRef)
class ResearchRefAdmin(admin.ModelAdmin):
    list_display = ('device', 'status', 'date_start', 'date_finish')
    list_filter = ('device', 'status', 'date_start', 'date_finish')
    search_fields = ('device', 'status', 'date_start', 'date_finish')
