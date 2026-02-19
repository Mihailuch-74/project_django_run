from django.contrib import admin
from django.urls import path, include
from app_run import views
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/runs", views.RunViewSet)
router.register("api/users", views.UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/company_details/", views.company_details),
    path("", include(router.urls)),
] + debug_toolbar_urls()
