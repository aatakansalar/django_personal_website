from django.contrib import admin
from post.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["post_title", "post_author", "post_date"]
    list_display_links = ["post_title", "post_author", "post_date"]

    search_fields = ["post_title"]
    list_filter = ["post_date"]

    class Meta:
        model = Post