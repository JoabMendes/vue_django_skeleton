# Domain
from domain.models import Member

# Rest Framework libraries
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
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

    '''
    def post(self, request, format=None):

        user_location = request.data['location']
        ration = request.data['ratio']
    '''
