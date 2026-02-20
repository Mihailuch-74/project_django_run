from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter

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


class PagePagination(PageNumberPagination):
    page_size_query_param = "size"
    max_page_size = 5


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["first_name", "last_name"]
    ordering_fields = ["date_joined"]
    pagination_class = PagePagination

    def get_queryset(self):
        qs = self.queryset
        type = self.request.query_params.get("type", None)

        if type == "coach":
            qs = qs.filter(is_staff=True)

        elif type == "athlete":
            qs = qs.filter(is_staff=False)

        return qs


class RunViewSet(ModelViewSet):
    queryset = Run.objects.select_related("athlete")
    serializer_class = RunSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["status", "athlete"]
    ordering_fields = ["created_at"]
    pagination_class = PagePagination


class RunStartApiView(APIView):
    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("id")

        try:
            run = Run.objects.get(id=id)

            if run.status == "init":
                run.status = "in_progress"
                run.save()
                data = {"message": "Забег начат"}
                return Response(data, status=status.HTTP_200_OK)

            else:
                data = {
                    "message": "Невозможно запустить запущенный или законченный забег"
                }

                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        except Run.DoesNotExist:
            data = {"message": "Забег не найден"}

        return Response(data, status=status.HTTP_404_NOT_FOUND)


class RunStopApiView(APIView):
    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("id")

        try:
            run = Run.objects.get(id=id)

            if run.status == "in_progress":
                run.status = "finished"
                run.save()
                data = {"message": "Забег окончен"}
                return Response(data, status=status.HTTP_200_OK)

            else:
                data = {"message": "Невозможно закончить не начатый забег"}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        except Run.DoesNotExist:
            data = {"message": "Забег не найден"}

        return Response(data, status=status.HTTP_404_NOT_FOUND)
