from django.conf.urls import url
from . import views
from django.urls import include
from rest_framework import routers

router = routers.SimpleRouter()
router.register('Users', views.UserMixins)

urlpatterns = [
    url(r'', include(router.urls))
]
