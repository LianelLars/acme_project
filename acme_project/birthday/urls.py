from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    path('', views.birthday, name='create'),
    path('list/', views.birthday_list, name='list'),
    path('<int:pk>/edit/', views.birthday, name='edit'),
    path('<int:pk>/delete/', views.delete_birthday, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
