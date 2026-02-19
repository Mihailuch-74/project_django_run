from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from rest_framework.viewsets import ModelViewSet

from app_run.models import Run
from app_run.serializers import RunSerializer


@api_view(["GET"])
def company_details(request):
    company_name = settings.СOMPANY_NAME
    slogan = settings.SLOGAN
    contacts = settings.CONTACTS

    return Response(
        {"company_name": company_name, "slogan": slogan, "contacts": contacts}
    )


class RunViewSet(ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
