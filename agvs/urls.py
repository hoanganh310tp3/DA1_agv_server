from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
 
router.register('post', views.AgvDataViewSet, basename="post" )

urlpatterns = [
    path("", view=views.index),
]
urlpatterns += router.urls