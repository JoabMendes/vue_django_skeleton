from django.contrib import admin

# Register your models here.
from domain.models import Stamp, Sector, Member, Reviewer, Review


class StampAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'created_at'
    )
    search_fields = ['title']


class SectorAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'updated_at'
    )
    search_fields = ['title']


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'created_at', 'active', 'featured'
    )
    list_filter = ['name', 'featured', 'stamps', 'sectors']
    search_fields = ['name']


class ReviewerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'created_at'
    )
    search_fields = ['name', 'email']


class ReviewAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'approved']
    search_field = ['comment']


admin.site.register(Stamp, StampAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Reviewer, ReviewerAdmin)
admin.site.register(Review, ReviewAdmin)
