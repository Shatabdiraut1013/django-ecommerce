# Generated by Django 3.2 on 2021-06-08 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_thibnail_blogpost_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='tile',
            new_name='title',
        ),
    ]