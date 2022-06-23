from django.contrib import admin
from add.models import Patient
# Register your models here.

class PatientAdmin(admin.ModelAdmin ):
    list_display = ['name', 'phone', 'email', 'gender','age', 'created_at']
    search_fields = ['name', 'phone', 'email', 'gender', 'note','age']
    list_filter = ['gender']
    list_per_page = 2
    
    

admin.site.register(Patient, PatientAdmin)