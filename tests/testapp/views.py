
from rest_framework import pagination, viewsets

from rest_framework_filters import backends

from .filters import DFUserFilter, NoteFilter, UserFilter
from .models import Note, User
from .serializers import NoteSerializer, UserSerializer


class DFUserViewSet(viewsets.ModelViewSet):
    # used to test compatibility with the drf-filters backend
    # with standard django-filter FilterSets.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [backends.RestFrameworkFilterBackend]
    filterset_class = DFUserFilter


class FilterClassUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [backends.RestFrameworkFilterBackend]
    filterset_class = UserFilter


class FilterFieldsUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [backends.RestFrameworkFilterBackend]
    filterset_fields = {
        'username': '__all__',
    }


class UnfilteredUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [backends.RestFrameworkFilterBackend]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [backends.RestFrameworkFilterBackend]
    filterset_class = UserFilter


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [backends.RestFrameworkFilterBackend]
    filterset_class = NoteFilter
