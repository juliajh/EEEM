# Generated by Django 3.2.7 on 2021-11-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_manner_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='manner',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
