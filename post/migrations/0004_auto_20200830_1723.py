# Generated by Django 3.1 on 2020-08-30 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-post_date']},
        ),
    ]
