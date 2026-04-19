from django.urls import path
from . import views

app_name = "calculator"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("result/<int:pk>/", views.result, name="result"),
    # path("calculator/<int:id>/", views.calculator, name="age_calc"),
]
