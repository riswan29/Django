# Generated by Django 4.1.3 on 2022-11-19 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('kontent', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
