# Generated by Django 3.2.6 on 2021-11-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211110_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='coin',
            field=models.IntegerField(default=0),
        ),
    ]
