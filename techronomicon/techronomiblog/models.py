from django.db import models
from markdownx.models import MarkdownxField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = MarkdownxField()  # Use MarkdownxField for Markdown support
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
