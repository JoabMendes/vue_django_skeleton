
# Domain
from domain.models import Review

# Rest Framework libraries
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Serializers
from api.serializers import ReviewSerializer
from api.serializers import WriteReviewSerializer


class ReviewAPIView(APIView):

    permission_classes = ()

    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404

    def post(self, request, id, format=None):
        """" POST /api/v1/review/

             Creates a review

             payload: {
                reviewer: {
                    name: 'name',
                    email: 'valid@mail.com'
                }
                stars: 4,
                comment: ''
             }
        """
        serializer = WriteReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request, id, format=None):
        """" GET /api/v1/review/<id>

            Retrieves a review by the specified id
        """
        review = self.get_object(pk=id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
