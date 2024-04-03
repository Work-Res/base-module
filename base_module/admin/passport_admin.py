from django.contrib import admin

from ..models import Passport
from ..forms import PassportForm


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
	form = PassportForm
