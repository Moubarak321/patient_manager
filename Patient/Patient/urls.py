"""Patient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from xml.etree.ElementInclude import include
from add import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Acces the frontend page
    path('', views.frontend, name='frontend'),

    # login /// logout
    path('login/', include('django.contrib.auth.urls')),
 
    # ======= BACKEND Section =======
    path('backend/', views.backend, name='backend'),
    
    # ======= path to add patient =======
    path('add_patient/', views.add_patient, name='add_patient'),
    
    # ======= path to access individual data =======
    path('patient/<str:patient_id>', views.patient, name='patient'),
    
    # ======= path to edit patient =======
    path('edit_patient/', views.edit_patient, name='edit_patient'),
    
    # ======= path to delete data =======
    path('delete_patient/<str:patient_id>', views.delete_patient, name='delete_patient'),
        
]
