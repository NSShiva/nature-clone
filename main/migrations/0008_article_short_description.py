# Generated by Django 3.0.5 on 2021-02-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210224_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
