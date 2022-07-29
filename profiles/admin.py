from django.contrib import admin

from profiles.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "address")
    list_filter = ("city",)
    search_fields = ("address",)
