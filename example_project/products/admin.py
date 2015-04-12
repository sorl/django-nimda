from django.contrib import admin
from .models import *


class ProductCategoryInline(admin.TabularInline):
    model = ProductCategory


class OptionValueInline(admin.TabularInline):
    model = OptionValue


class VariantInline(admin.TabularInline):
    model = Variant


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductCategoryInline]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [VariantInline]


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    inlines = [OptionValueInline]
