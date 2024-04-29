from django.contrib import admin
from .models import AdmissionForm, Contact


admin.site.site_header = "Marksman Club Admin"
admin.site.site_title = "The Marksman Club Admin"
admin.site.index_title = "Welcome to The Marksman Club Admin"

# Register your models here.
admin.site.register(AdmissionForm)
admin.site.register(Contact)
