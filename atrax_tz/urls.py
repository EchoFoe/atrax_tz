from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('phonebook.api.api_urls', namespace='phonebook_api')),
    # path('celery/', include('django_celery_beat.urls')),
    path('', include('phonebook.web_urls', namespace='phonebook_web')),
]
