from django.urls import include, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('df-users', views.DFUserViewSet, basename='df-users')
router.register('ff-users', views.FilterFieldsUserViewSet, basename='ff-users')
router.register('users', views.UserViewSet)
router.register('notes', views.NoteViewSet)


urlpatterns = [
    re_path(r'^', include(router.urls)),
]
