
from rest_framework import serializers
from recaptcha.fields import ReCaptchaField

from domain.models import Stamp, Sector, Member, Reviewer, Review


class StampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stamp
        fields = '__all__'


class SectorSerializer(serializers.ModelSerializer):

    icon = serializers.SerializerMethodField()

    class Meta:
        model = Sector
        fields = (
            'id',
            'title',
            'icon',
            'created_at',
            'updated_at'
        )

    def get_icon(self, sector):
        return sector.icon.id


class ReviewerSerializer(serializers.ModelSerializer):

    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Reviewer
        fields = '__all__'

    def get_avatar(self, reviewer):
        return reviewer.get_avatar_url()


class ReviewSerializer(serializers.ModelSerializer):

    reviewer = ReviewerSerializer()

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


class WriteReviewSerializer(serializers.ModelSerializer):

    reviewer = ReviewerSerializer()
    recaptcha = ReCaptchaField(write_only=True)

    class Meta:
        model = Review
        fields = (
            'member',
            'recaptcha',
            'reviewer',
            'stars',
            'comment'
        )

    def get_object_by_email(self, email):
        try:
            return Reviewer.objects.get(email=email)
        except Reviewer.DoesNotExist:
            return False

    def create(self, validated_data):
        del validated_data['recaptcha']
        reviewer_data = validated_data.pop('reviewer')
        reviewer = self.get_object_by_email(email=reviewer_data.get('email'))
        if not isinstance(reviewer,  Reviewer):
            reviewer = Reviewer.objects.create(**reviewer_data)
            reviewer.save()
        review = Review.objects.create(
            member=validated_data.get('member'),
            reviewer=reviewer,
            stars=validated_data.get('stars'),
            comment=validated_data.get('comment')
        )
        return review


class MemberSerializer(serializers.ModelSerializer):

    stars_average = serializers.SerializerMethodField()
    last_review = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = '__all__'
        depth = 1

    def get_stars_average(self, member):
        return member.get_stars_average()

    def get_last_review(self, member):
        review = Review.objects.filter(
            member=member, approved=True
        ).last()
        if review:
            serializer = ReviewSerializer(review)
            return serializer.data
        return {}

    def get_latitude(self, member):
        return member.position.latitude

    def get_longitude(self, member):
        return member.position.longitude


class MemberMapSerializer(serializers.ModelSerializer):

    stars_average = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = (
            'name',
            'latitude',
            'longitude',
            'photo',
            'logo',
            'stars_average'
        )

    def get_stars_average(self, member):
        return member.get_stars_average()

    def get_latitude(self, member):
        return member.position.latitude

    def get_longitude(self, member):
        return member.position.longitude
