from django.http import HttpRequest
from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from rest_framework import filters as drf_filters
from rest_framework.request import Request

from .models import ProfileType, SiteProfile
from .permissions import OrganizationPermission
from .serializers import ProfileTypeSerializer, SiteProfileSerializer
from . import filters


class ProfileTypeViewSet(viewsets.ModelViewSet):
    """

    retrieve:
    Retrieves a ProfileType by its ID.

    Retrieves a ProfileType by its ID.

    list:
    Retrieves a list of ProfileTypes.

    Retrieves a list of ProfileTypes.

    create:
    Creates a new ProfileType.

    Creates a new ProfileType.

    update:
    Updates the ProfileType with the given ID (all fields).

    Updates the ProfileType with the given ID (all fields).

    partial_update:
    Updates the ProfileType with the given ID (only specified fields).

    Updates the ProfileType with the given ID (only specified fields).

    destroy:
    Deletes the ProfileType with the given ID.

    Deletes the ProfileType with the given ID.

    """
    def get_queryset(self):
        queryset = super().get_queryset()
        organization_uuid = self.request.session['jwt_organization_uuid']
        queryset = queryset.filter(organization_uuid=organization_uuid)
        return queryset

    def _extend_request(self, request):
        data = request.data.copy()
        data['organization_uuid'] = request.session['jwt_organization_uuid']
        request_extended = Request(HttpRequest())
        request_extended._full_data = data
        return request_extended

    def create(self, request, *args, **kwargs):
        request_extended = self._extend_request(request)
        return super().create(request_extended, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request_extended = self._extend_request(request)
        return super().update(request_extended, *args, **kwargs)

    queryset = ProfileType.objects.all()
    permission_classes = (OrganizationPermission,)
    serializer_class = ProfileTypeSerializer
    filter_backends = (drf_filters.OrderingFilter,)
    ordering = ('name',)


class SiteProfileViewSet(viewsets.ModelViewSet):
    """

    retrieve:
    Retrieves a SiteProfile by its UUID.

    Retrieves a SiteProfile by its UUID.

    list:
    Retrieves a list of SiteProfiles.

    Retrieves a list of SiteProfiles.

    create:
    Creates a new SiteProfile.

    Creates a new SiteProfile.

    partial_update:
    Updates the SiteProfile with the given UUID (only specified fields).

    Updates the SiteProfile with the given UUID (only specified fields).

    update:
    Updates the SiteProfile with the given UUID (all fields).

    Updates the SiteProfile with the given UUID (all fields).

    destroy:
    Deletes the SiteProfile with the given UUID.

    Deletes the SiteProfile with the given UUID.

    """
    def get_queryset(self):
        queryset = super().get_queryset()
        organization_uuid = self.request.session['jwt_organization_uuid']
        queryset = queryset.filter(organization_uuid=organization_uuid)
        return queryset

    def _extend_request(self, request):
        data = request.data.copy()
        data['organization_uuid'] = request.session['jwt_organization_uuid']
        request_extended = Request(HttpRequest())
        request_extended._full_data = data
        return request_extended

    def create(self, request, *args, **kwargs):
        request_extended = self._extend_request(request)
        return super().create(request_extended, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request_extended = self._extend_request(request)
        return super().update(request_extended, *args, **kwargs)

    filter_backends = (django_filters.DjangoFilterBackend,
                       drf_filters.SearchFilter,
                       drf_filters.OrderingFilter)
    filter_class = filters.SiteProfileFilter
    ordering = ('name',)
    permission_classes = (OrganizationPermission,)
    queryset = SiteProfile.objects.all()
    serializer_class = SiteProfileSerializer
    search_fields = ('address_line1', 'postcode', 'city', )
