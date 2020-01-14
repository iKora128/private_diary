
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include

from . import setting_common, setting_dev


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("private_app.urls")),
    path("accounts/", include("allauth.urls"))
]

urlpatterns += static(setting_common.MEDIA_URL, document_root=setting_dev.MEDIA_ROOT)

