from django.urls import path
from .views import UploadCVView,index

urlpatterns = [
    path('',index,name='index'),
    path('upload-cv/', UploadCVView.as_view(), name='upload-cv')
]

