

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rango import views
from django.urls import include

urlpatterns = [
    path('',views.index, name='index'),
    path('rango/',include('rango.urls')),
    path('rango/about/',views.about),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
