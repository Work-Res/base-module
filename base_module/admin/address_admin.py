from django.contrib import admin

from ..models import Address
from ..forms import AddressForm


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	form = AddressForm
