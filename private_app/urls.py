from django.urls import path
from .views import IndexView, InquiryView

app_name = "private_app"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("inquiry/", InquiryView.as_view(), name="inquiry"),
]
