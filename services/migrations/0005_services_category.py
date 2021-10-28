# Generated by Django 3.2.8 on 2021-10-28 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_alter_blogs_date'),
        ('services', '0004_auto_20211027_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='blogs.category'),
            preserve_default=False,
        ),
    ]
