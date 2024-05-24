from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views as v

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',v.home),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print(static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))
