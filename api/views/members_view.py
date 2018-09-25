# Domain
from domain.models import Member

# Rest Framework libraries
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.custom_permissions import IsGetOrIsAuthenticated

# Serializers
from api.serializers import MemberSerializer, MemberMapSerializer


class MemberAPIView(APIView):

    permission_classes = (IsGetOrIsAuthenticated,)

    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk, active=True)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        member = self.get_object(pk=id)
        serializer = MemberSerializer(member)
        return Response(serializer.data)


class FeaturedMemberAPIView(APIView):

    permission_classes = (IsGetOrIsAuthenticated,)

    def get(self, format=None):
        featured_members = Member.objects.filter(featured=True, active=True)
        serializer = MemberSerializer(featured_members, many=True)
        return Response(serializer.data)


class MemberMapAPIView(APIView):

    def get(self, format=None):
        all_members = Member.objects.filter(active=True)
        serializer = MemberMapSerializer(all_members, many=True)
        return Response(serializer.data)

    def validate_location(self, location):
        max_lat = 90
        min_lat = -90
        max_long = 180
        min_long = -180
        if 'lat' in location:
            if location['lat'] >= max_lat and location['lat'] <= min_lat:
                return False
        else:
            return False
        if 'long' in location:
            if location['long'] >= max_long and location['long'] <= min_long:
                return False
        else:
            return False
        return True

    def post(self, request, format=None):

        if 'location' in request.data and 'ratio' in request.data:
            location = request.data['location']
            if self.validate_location(location):
                ratio = request.data['ratio']
                lat = location['lat']
                long = location['long']
                members = Member.objects.all()
                metric = 'km'
                if 'metric' in request.data and request.data['metric'] != 'km':
                    metric = 'ml'
                near_members = []
                for member in members:
                    if member.is_near(lat, long, ratio, metric):
                        near_members.append(member)
                serializer = MemberMapSerializer(near_members, many=True)
                return Response(serializer.data)
            else:
                error = {
                    'message': 'Invalid location specified',
                    'error': 'Invalid location paramenter'
                }
                return Response(
                    error, status=status.HTTP_422_UNPROCESSABLE_ENTITY
                )
        else:
            error = {
                'message': 'missing location or ratio paramenters',
                'error': 'missing parameter'
            }
            return Response(
                error, status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
