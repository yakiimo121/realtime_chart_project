from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('realtimechart/', include('realtime_chart.urls')),
    path('admin/', admin.site.urls),
]