# Generated by Django 3.2.8 on 2021-11-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0013_rename_auditorialboardmodel_auditorialboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('shortdes', models.TextField(max_length=300)),
                ('logo', models.ImageField(upload_to='certificatelogo')),
                ('Certificate', models.FileField(blank=True, upload_to='certificates')),
            ],
        ),
    ]
