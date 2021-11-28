from enum import unique
from django.db.models import query
from rest_framework import serializers

from user_mbe.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    id                      = serializers.PrimaryKeyRelatedField(read_only=True)
    first_name              = serializers.CharField(max_length=120)
    last_name               = serializers.CharField(max_length=120)
    id_number               = serializers.CharField(max_length=30)
    phone_number            = serializers.CharField(max_length=15)
    email                   = serializers.EmailField()
    job_title               = serializers.CharField(max_length=100)

    class Meta:
        model = Employee
        fields = [
            "id",
            "first_name",
            "last_name",
            "id_number",
            "phone_number",
            "email",
            "job_title"
        ]

    def validate_email(self, value):

        queryset = Employee.objects.filter(email=value, created_by=self.context.get("view").request.user)

        if (
            self.instance is None and queryset.exists()
        ) or (
            self.instance and queryset.exclude(id=self.instance.id).exists()
        ):

            # Raise Error
            raise serializers.ValidationError(detail="Email Id already exists.")

        return value
