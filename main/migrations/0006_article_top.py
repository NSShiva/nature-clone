# Generated by Django 3.1.7 on 2021-02-24 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='top',
            field=models.BooleanField(default=False),
        ),
    ]
