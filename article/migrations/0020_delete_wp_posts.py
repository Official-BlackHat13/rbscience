# Generated by Django 3.2.8 on 2021-11-10 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_artical'),
    ]

    operations = [
        migrations.DeleteModel(
            name='wp_posts',
        ),
    ]