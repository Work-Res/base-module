from django.contrib import admin

from ..models import Person
from ..forms import PersonForm


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	form = PersonForm
