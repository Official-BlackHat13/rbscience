# Generated by Django 3.2.8 on 2021-10-28 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_alter_blogs_blog_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
