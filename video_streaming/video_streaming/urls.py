from apps.users.views import Login, Logout
from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    re_path(r"^api/", include("apps.users.api.routers")),
    re_path(r"^api/", include("apps.video.api.routers")),
    re_path(r"^api/", include("apps.playlist.api.routers")),
    re_path(r"^api/", include("apps.season.api.routers")),
    re_path(r"^api/", include("apps.core.api.routers")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
