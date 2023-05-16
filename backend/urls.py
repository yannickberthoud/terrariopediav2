from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import register, view_login, view_logout

from .views import index

urlpatterns = [
    path('', index, name="home"),
    path('admin/', admin.site.urls),
    path('unicorn/', include("django_unicorn.urls")),
    path('fiches-d-elevage/', include('card.urls', namespace="card")),
    path('petites-annonces/', include('ads.urls', namespace="ads")),
    path("terrariopedia/", include("django.contrib.flatpages.urls")),
    path("communaute/", include('member.urls', namespace="member")),
    path("documentations/", include('documentation.urls', namespace="documentation")),
    path("register", register, name="register"),
    path("login", view_login, name="login"),
    path("logout", view_logout, name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
