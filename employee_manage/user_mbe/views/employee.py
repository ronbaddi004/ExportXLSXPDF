from typing import List
from django.db import transaction
from rest_framework import serializers

# from drf_renderer_xlsx.renderers import XLSXRenderer
# from drf_renderer_xlsx.mixins import XLSXFileMixin

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from user_mbe.renderers import PDFRenderer, XLSXRenderer

from user_mbe.models import Employee
from user_mbe.serializers.employee import EmployeeSerializer


class EmployeeAPIView(ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = [PDFRenderer, XLSXRenderer, JSONRenderer]

    def get_queryset(self):
        return Employee.objects.filter(created_by=self.request.user)

    def get(self, request, *args, **kwargs):

        header = None
        if request.query_params.get("format", "").lower() == 'pdf':
            header = {'Content-Disposition': 'attachment; filename=employee_list.pdf'}
        if request.query_params.get("format", "").lower() == 'xlsx':
            header = {'Content-Disposition': 'attachment; filename=employee_list.xlsx'}

        response = super().list(request, *args, **kwargs)
        if request.query_params.get("format", "").lower() == 'pdf' or request.query_params.get("format", "").lower() == 'xlsx':
            response.headers = header

        return response


class EmployeeListCreateAPIView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Employee.objects.filter(created_by=self.request.user)

    def get_serializer_context(self):
        return {"view": self}

    def perform_create(self, serializer):

        if serializer.is_valid(raise_exception=True):

            with transaction.atomic():

                # save model
                serializer.save(created_by=self.request.user)


class EmployeeRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Employee.objects.filter(created_by=self.request.user)

    def get_object(self):
        return self.get_queryset().get(id=self.kwargs.get("id"))

    def get_serializer_context(self):
        return {"view": self}

    def perform_update(self, serializer):

        if serializer.is_valid(raise_exception=True):

            with transaction.atomic():

                # save model
                serializer.save()

    def perform_destroy(self, instance):

        with transaction.atomic():

            instance.delete()
