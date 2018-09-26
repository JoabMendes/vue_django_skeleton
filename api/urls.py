from django.conf.urls import url

from api.views import stamps_view
from api.views import sectors_view
from api.views import members_view
from api.views import review_view

urlpatterns = [
    url(
        r'^stamps/(?P<id>[0-9]+)?/?$',
        stamps_view.StampAPIView.as_view()
    ),
    url(
        r'^stamps/member/(?P<member_id>[0-9]+)/?$',
        stamps_view.StampMemberAPIView.as_view()
    ),
    url(
        r'^sectors/(?P<id>[0-9]+)?/?$',
        sectors_view.SectorAPIView.as_view()
    ),
    url(
        r'^sectors/member/(?P<member_id>[0-9]+)/?$',
        sectors_view.SectorMemberAPIView.as_view()
    ),
    url(
        r'^members/(?P<id>[0-9]+)/?$',
        members_view.MemberAPIView.as_view()
    ),
    url(
        r'^members/featured/?$',
        members_view.FeaturedMemberAPIView.as_view()
    ),
    url(
        r'^members/map/?$',
        members_view.MemberMapAPIView.as_view()
    ),
    url(
        r'^reviews/(?P<id>[0-9]+)?/?$',
        review_view.ReviewAPIView.as_view()
    )
]
