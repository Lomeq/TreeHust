# Generated by Django 4.1 on 2022-11-05 10:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Post", "0003_rename_created_at_comment_last_modified_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post", name="stars", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="post",
            name="vote",
            field=models.ManyToManyField(
                blank=True,
                related_name="user_vote",
                to=settings.AUTH_USER_MODEL,
                verbose_name="vote by some user",
            ),
        ),
    ]