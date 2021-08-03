import django
from channels.http import AsgiHandler
# from channels.routing import ProtocolTypeRouter

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.server')
# django.setup()

# application = ProtocolTypeRouter({
#   "http": AsgiHandler(),
#   # Just HTTP for now. (We can add other protocols later.)
# })
# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# import chat.routing
from delivery.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zomato.settings')
django.setup()


application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  "websocket": 
        URLRouter(
            websocket_urlpatterns
        ),
})