from django.db import models
from markdownx.models import MarkdownxField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = MarkdownxField()  # Use MarkdownxField for Markdown support
    pub_date = models.DateTimeField(auto_now_add=True)
    og_title = models.CharField(max_length=200, blank=True)
    og_description = models.TextField(blank=True)
    og_image = models.ImageField(upload_to='og_images/', blank=True)
    
    def get_truncated_content(self):
        return self.content[:500] + '...' if len(self.content) > 500 else self.content

    def __str__(self):
        return self.title

class AboutPage(models.Model):
    content = MarkdownxField()
