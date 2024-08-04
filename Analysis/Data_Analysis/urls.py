from django.urls import path
from .views import UploadFileAPIView, ResultsAPIView

urlpatterns = [
    path('', UploadFileAPIView.as_view(), name='upload'),  # Route to upload view
    path('results/', ResultsAPIView.as_view(), name='results'),  # Route to results view
]
