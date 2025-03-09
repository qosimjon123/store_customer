from django.contrib import admin
from django.contrib.admin import TabularInline
from django.contrib.contenttypes.admin import GenericTabularInline

from Customer.models import Client, ClientAddress


class ClientAddressInline(admin.TabularInline):
    model = ClientAddress



class CustomerAdmin(admin.ModelAdmin):
    inlines = [ClientAddressInline]


admin.site.register(Client, CustomerAdmin)