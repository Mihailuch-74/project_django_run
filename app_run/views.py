from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from app_run.models import Run
from app_run.serializers import RunSerializer, UserSerializer


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


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = self.queryset
        type = self.request.query_params.get("type", None)

        if type == "coach":
            qs = qs.filter(is_staff=True)

        elif type == "athlete":
            qs = qs.filter(is_staff=False)

        return qs
