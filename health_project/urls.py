from django.contrib import admin
from django.urls import path
from health_project_server import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index)
]
