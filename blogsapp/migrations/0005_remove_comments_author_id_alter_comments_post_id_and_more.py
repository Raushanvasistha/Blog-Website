# Generated by Django 5.1 on 2024-08-27 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsapp', '0004_rename_bid_comments_cid_alter_blog_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='Author_id',
        ),
        migrations.AlterField(
            model_name='comments',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cbid', to='blogsapp.blog'),
        ),
        migrations.AddField(
            model_name='comments',
            name='author_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
