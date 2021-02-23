from django.contrib import admin
from .models import people,peopleAdmin
from .models import products,productsAdmin

admin.site.register(people,peopleAdmin)
admin.site.register(products,productsAdmin)
