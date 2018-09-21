from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import hashlib

# Create your models here.


class Stamp(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    image = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to='stamp_files',
        blank=True,
        null=True
    )
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Stamp'
        verbose_name_plural = 'Stamps'


class Sector(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectors'


class Member(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    latitude = models.CharField(max_length=128, blank=False, null=False)
    longitude = models.CharField(max_length=128, blank=False, null=False)
    open_hours = models.TextField(blank=False, null=False)
    products = models.TextField(blank=False, null=False)
    sectors = models.ManyToManyField(Sector, related_name='sectors')
    stamps = models.ManyToManyField(Stamp, related_name='stamps')
    logo = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to='member_logos',
        blank=True,
        null=True
    )
    photo = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to='member_logos',
        blank=True,
        null=True
    )
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def get_stars_average(self):
        all_reviews = Review.objects.filter(member=self)
        if all_reviews.count():
            sum = 0
            for review in all_reviews:
                sum += review.stars
            return sum / all_reviews.count()
        return 0


class Reviewer(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    email = models.CharField(max_length=256, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def get_avatar_url(self):
        md5 = hashlib.md5(self.email.encode())
        digest = md5.hexdigest()
        return 'http://www.gravatar.com/avatar/{0}?d=404'.format(digest)

    class Meta:
        verbose_name = 'Reviewer'
        verbose_name_plural = 'Reviewers'


class Review(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    stars = models.IntegerField(null=False, blank=False)
    comment = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return '{0} ({1})'.format(
            self.reviewer.name, self.created_at.strftime('%m-%d-%Y')
        )

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
