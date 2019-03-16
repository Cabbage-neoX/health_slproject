from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/',TemplateView.as_view(template_name='index.html'))
]