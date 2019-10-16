#post model
from django.contrib import admin

# Register your models here.
#models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin."""

    list_display = ('id', 'user', 'title', 'photo')
    search_field = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'modified')
