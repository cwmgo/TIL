# Generated by Django 2.2.4 on 2019-08-08 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_updatated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='updatated_at',
            new_name='updated_at',
        ),
    ]
