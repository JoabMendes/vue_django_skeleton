# Domain
from domain.models import Reviewer

# Rest Framework libraries
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Serializers
from api.serializers import ReviewerSerializer


class ReviewerAPIView(APIView):

    permission_classes = ()

    def get_object(self, pk):
        try:
            return Reviewer.objects.get(pk=pk)
        except Reviewer.DoesNotExist:
            raise Http404

    def get_object_by_email(self, email):
        try:
            return Reviewer.objects.get(email=email)
        except Reviewer.DoesNotExist:
            return False

    def get(self, request, id, format=None):
        """" GET /api/v1/reviewer/<id>

            Retrieves a reviewer by the specified id
        """
        reviewer = self.get_object(pk=id)
        serializer = ReviewerSerializer(reviewer)
        return Response(serializer.data)

    def post(self, request, id, format=None):
        """" POST /api/v1/reviewer/

            Creates a reviewer

            payload: {
                name: 'name',
                email: 'valid@mail.com'
            }
        """
        serializer = ReviewerSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data['email'].strip()
            object = self.get_object_by_email(email=email)
            if isinstance(object, Reviewer):
                serializer = ReviewerSerializer(object)
            else:
                reviewer = Reviewer(
                    name=request.data['name'].strip(),
                    email=request.data['email'].strip()
                )
                reviewer.save()
                serializer = ReviewerSerializer(reviewer)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
