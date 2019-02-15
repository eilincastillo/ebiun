"""Ebiun urls"""

# Django
from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


from .views import index

urlpatterns = [
    path('admin/',
         admin.site.urls),

    path('servicios/', include(('services.urls','services'), namespace='sevices')),
    path('estudiantes/', include(('student.urls','student'), namespace='student')),
    path('', index, name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)