
from rest_framework import serializers


from domain.models import Stamp, Sector, Member, Reviewer, Review


class StampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stamp
        fields = '__all__'


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class ReviewerSerializer(serializers.ModelSerializer):

    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Reviewer
        fields = '__all__'

    def get_avatar(self, reviewer):
        return reviewer.get_avatar_url()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'reviewer',
            'stars',
            'comment',
            'approved',
            'created_at',
            'updated_at'
        )
        depth = 1


class MemberSerializer(serializers.ModelSerializer):

    stars_average = serializers.SerializerMethodField()
    last_review = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = '__all__'
        depth = 1

    def get_stars_average(self, member):
        return member.get_stars_average()

    def get_last_review(self, member):
        return ReviewSerializer(
            Review.objects.filter(member=member).last()
        ).data
