from django.contrib import admin
from .models import Post, Headline


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['published', 'created']
    search_fields = ['title', 'description', 'content']
    date_hierarchy = 'created'
    save_on_top = True


class HeadLineAdmin(admin.ModelAdmin):
    list_display = ['headline']
    list_filter = ['created', 'is_current']
    date_hierarchy = 'created'
    save_on_top = True


admin.site.register(Post, PostAdmin)
admin.site.register(Headline, HeadLineAdmin)