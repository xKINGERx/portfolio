from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
