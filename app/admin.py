from django.contrib import admin
from django.utils.html import format_html
from .models import Banner, AboutUs, Service, Gallery, MeetOurTeam, Testimonial,AboutBusiness

admin.site.site_header = "Prime Hub"
admin.site.site_title = "Prime Hub"
admin.site.index_title = "Prime Hub"


# ---------- BANNER ----------
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:8px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"


# ---------- ABOUT US ----------
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:8px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"


@admin.register(AboutBusiness)
class AboutBusiness(admin.ModelAdmin):
    list_display = ("id","image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:8px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"


# ---------- SERVICE ----------
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview")
    search_fields = ("title", "description")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:8px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"


# ---------- GALLERY ----------
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:8px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"


# ---------- TEAM ----------
@admin.register(MeetOurTeam)
class MeetOurTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "photo_preview")
    search_fields = ("name", "position")
    readonly_fields = ("photo_preview",)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" style="border-radius:50%;" />', obj.photo.url)
        return "No Image"

    photo_preview.short_description = "Preview"


# ---------- TESTIMONIAL ----------
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "short_feedback")
    search_fields = ("name", "position", "feedback")

    def short_feedback(self, obj):
        return obj.feedback[:60] + "..."

    short_feedback.short_description = "Feedback"
