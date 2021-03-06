from django.urls import path

from tracker.views import MapGraphQLTemplateView
from tracker.views import MapRESTTemplateView

urlpatterns = [
    path("graph-api/", MapGraphQLTemplateView.as_view(), name="graph-map"),
    path("rest-api/", MapRESTTemplateView.as_view(), name="rest-map"),
]
