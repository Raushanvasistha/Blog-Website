# Generated by Django 5.1 on 2024-08-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsapp', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='bid',
            new_name='cid',
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
