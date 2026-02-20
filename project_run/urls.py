from django.contrib import admin
from django.urls import path, include
from app_run import views
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/runs", views.RunViewSet)
router.register("api/users", views.UserViewSet)
router.register("api/challenges", views.ChallengesViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/company_details/", views.company_details),
    path("api/runs/<int:id>/start/", views.RunStartApiView.as_view()),
    path("api/runs/<int:id>/stop/", views.RunStopApiView.as_view()),
    path("api/athlete_info/<int:user_id>/", views.AthleteInfoApiView.as_view()),
    path("", include(router.urls)),
] + debug_toolbar_urls()
