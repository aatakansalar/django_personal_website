from django.contrib import admin
from post.models import Post, Tag
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["post_title", "post_author", "post_date"]
    list_display_links = ["post_title", "post_author", "post_date"]

    search_fields = ["post_title", "post_tags"]
    list_filter = ["post_date"]

    class Meta:
        model = Post

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name','slug']
    list_display_links = ['tag_name','slug']
    class Meta: 
        model = Tag