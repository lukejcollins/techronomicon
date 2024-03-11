from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin
from .models import AboutPage

admin.site.register(Post, MarkdownxModelAdmin)

class AboutPageAdmin(MarkdownxModelAdmin):
    def has_add_permission(self, request):
        if AboutPage.objects.exists():
            return False
        return super().has_add_permission(request)

admin.site.register(AboutPage, AboutPageAdmin)
