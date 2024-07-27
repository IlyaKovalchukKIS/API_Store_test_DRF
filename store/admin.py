from django.contrib import admin

from store.models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "author",
        "created_at",
    )
