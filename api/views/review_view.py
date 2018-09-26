
# Domain
from domain.models import Review, Member

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


class MemberReviewAPIView(APIView):

    def get_member_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, member_id, format=None):
        """" GET /api/v1/reviews/member/<member_id>

             Retrieves all reviews related to a member
             payload for pagination:
             payload: {
                offset: 0 (Default),
                reviews_per_page: 10 (Default)
             }
        """
        offset = 0
        reviews_per_page = 10
        if 'offset' in request.data:
            offset = int(request.data['offset'])
        if 'reviews_per_page' in request.data:
            reviews_per_page = int(request.data['reviews_per_page'])
        member = self.get_member_object(pk=member_id)
        member_reviews = Review.objects.filter(
            member=member, approved=True
        )
        serializer = ReviewSerializer(
            member_reviews[offset:(offset+reviews_per_page)],
            many=True
        )
        response = dict()
        response['offset'] = offset
        response['reviews_per_page'] = reviews_per_page
        response['data'] = serializer.data
        return Response(response)
