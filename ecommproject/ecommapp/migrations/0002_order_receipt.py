# Generated by Django 5.0.1 on 2024-01-31 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='receipt',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
