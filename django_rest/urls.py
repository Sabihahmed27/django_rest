from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import urls,urlpatterns
from webapp import views

"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', views.employeeList.as_view(), name='employees'),  # 'views.employeeList.as_view()' will display Employees list data after serializing it
    # path('employees/', include('webapp.views')),
]
