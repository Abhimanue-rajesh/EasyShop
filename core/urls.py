from django.contrib import admin
from django.conf import settings

from django.urls import path, include, re_path
from django.views.static import serve


urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('', include("home.urls")),
    path('inventory/', include("inventory.urls")),
]
