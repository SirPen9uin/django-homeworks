from django.urls import path

from .views import SensorView, SensorRetriveUpdateAPIView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorRetriveUpdateAPIView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
