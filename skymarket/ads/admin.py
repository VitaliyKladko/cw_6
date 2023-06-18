from django.contrib import admin

from ads.models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'author', 'created_at')
    search_fields = ('title', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'ad', 'created_at')
    search_fields = ('author', )
