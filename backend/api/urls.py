from django.urls import path
from . import views

urlpatterns = [
    path("flooddata/", views.DataListView.as_view(), name="data-list"),
    path("flooddata/receive/", views.FloodDataAPIView.as_view(), name="receive-data"),
]
