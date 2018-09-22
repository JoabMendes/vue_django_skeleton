
# Domain
from domain.models import Sector, Member

# Rest Framework libraries
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from api.custom_permissions import IsGetOrIsAuthenticated
from rest_framework import status

# Serializers
from api.serializers import SectorSerializer


class SectorAPIView(APIView):

    permission_classes = (IsGetOrIsAuthenticated,)

    def get_object(self, pk):
        try:
            return Sector.objects.get(pk=pk)
        except Sector.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        """" GET /api/v1/sectors/<id>

        Retrieves a sector by the specified id
        """
        sector = self.get_object(pk=id)
        serializer = SectorSerializer(sector)
        return Response(serializer.data)

    def post(self, request, id, format=None):
        """" POST /api/v1/sectors

        Creates a sector with the specified body
        """
        serializer = SectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        """" PUT /api/v1/sectors/<id>

        Edits an sector information
        """
        sector = self.get_object(pk=id)
        serializer = SectorSerializer(sector, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id, format=None):
        """" DELETE /api/v1/sectors/<id>

            Deletes a specified sector
        """
        sector = self.get_object(pk=id)
        serializer = SectorSerializer(sector)
        serializer.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class SectorMemberAPIView(APIView):

    permission_classes = (IsGetOrIsAuthenticated,)

    def get_member_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, member_id, format=None):
        """" GET /api/v1/sectors/member/<member_id>

             Returns sectors related to a specific member
        """
        member = self.get_member_object(pk=member_id)
        serializer = SectorSerializer(member.sectors, many=True)
        return Response(serializer.data)
