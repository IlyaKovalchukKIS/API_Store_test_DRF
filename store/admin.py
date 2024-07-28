from django.contrib import admin

from store.models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "id_advertisement",
        "title",
        "author",
        "count_view",
        "position",
    )
