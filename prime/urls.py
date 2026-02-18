from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="service"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
]

# Always serve media (Railway fix)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
