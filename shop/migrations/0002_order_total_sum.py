# Generated by Django 4.2 on 2023-06-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Total_Sum',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
