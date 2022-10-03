from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('exam/', include('backend.exam.urls', namespace='exam')),
    path('admin/', admin.site.urls),
]
