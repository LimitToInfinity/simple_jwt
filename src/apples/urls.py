from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('apples', views.ApplesView)
router.register('users', views.UsersView)

urlpatterns = [
    path('', include(router.urls))
]
