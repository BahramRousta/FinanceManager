from django.contrib import admin
from .models import (
    Bank,
    Category,
    SubCategory,
    Transition
)

admin.site.register(Bank)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Transition)