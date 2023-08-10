from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/', views.get_details, name='get'),
    path('post/', views.post_details, name='post'),
    path('put/<int:pk>/', views.update_details, name='post'),
    path('delete/<int:pk>/', views.delete_details, name='delete')
    ]




