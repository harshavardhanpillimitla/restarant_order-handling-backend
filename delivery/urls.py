from django.urls import path, include

from .views import OrderViewset,GetUserDetails



from rest_framework import routers

router =  routers.DefaultRouter()
router.register(r'', OrderViewset)

urlpatterns=[
    path('getuser/',GetUserDetails.as_view()),
    path('', include(router.urls)),
    
]