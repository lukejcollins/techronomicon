# Generated by Django 4.2.10 on 2024-03-12 20:26

from django.db import migrations, models
import markdownx.models  # type: ignore


class Migration(migrations.Migration):

    dependencies = [
        ('techronomiblog', '0003_aboutpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='og_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='og_image',
            field=models.ImageField(blank=True, upload_to='og_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='og_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
