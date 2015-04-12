from django.contrib import admin
from .models import *


class OrderLineInline(admin.TabularInline):
    model = OrderLine


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline]
