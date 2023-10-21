from django.urls import path

from main.apps import MainConfig
from main.views import contact, StudentDetailView, StudentListView

app_name = MainConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('views/<int:pk>/', StudentDetailView.as_view(), name='view_student')
]
