from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin
from .models import AboutPage

class PostAdmin(MarkdownxModelAdmin):
    fields = ('title', 'content', 'og_title', 'og_description', 'og_image')

admin.site.register(Post, PostAdmin)

class AboutPageAdmin(MarkdownxModelAdmin):
    def has_add_permission(self, request):
        if AboutPage.objects.exists():
            return False
        return super().has_add_permission(request)

admin.site.register(AboutPage, AboutPageAdmin)
