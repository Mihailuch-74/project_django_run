from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.conf import settings


@api_view(["GET"])
def company_details(request):
    company_name = settings.СOMPANY_NAME
    slogan = settings.SLOGAN
    contacts = settings.CONTACTS

    return Response(
        {"company_name": company_name, "slogan": slogan, "contacts": contacts}
    )


# class CompanyDetails(APIView):
#     def get(self, request):
#         company_name = settings.СOMPANY_NAME
#         slogan = settings.SLOGAN
#         contacts = settings.CONTACTS
#
#         return Response(
#             {"company_name": company_name, "slogan": slogan, "contacts": contacts}
#         )
