from user_mbe.views.user import UserRegistrationCreateAPIView

from user_mbe.views.employee import EmployeeListCreateAPIView, EmployeeRUDAPIView, EmployeeAPIView

from django.urls import path


urlpatterns = [
    path("registration", UserRegistrationCreateAPIView.as_view()),

    path("employees/export", EmployeeAPIView.as_view()),
    path("employees", EmployeeListCreateAPIView.as_view()),
    path("employees/<int:id>", EmployeeRUDAPIView.as_view())
]
