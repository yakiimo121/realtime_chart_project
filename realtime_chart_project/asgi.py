import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import realtime_chart.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtime_chart_project.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            realtime_chart.routing.websocket_urlpatterns
        )
    ),
})