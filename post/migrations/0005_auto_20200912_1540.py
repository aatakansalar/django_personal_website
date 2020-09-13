# Generated by Django 3.1 on 2020-09-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200830_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_tags',
            field=models.ManyToManyField(to='post.Tags', verbose_name='tags'),
        ),
    ]