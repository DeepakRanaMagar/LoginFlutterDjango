from django.urls import path
from .views import EmailList

urlpatterns = [
    path('api/email', EmailList.as_view(), name="EmailList"),
]
