# Generated by Django 2.2.5 on 2021-04-12 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20210412_0732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='cleanliness',
            new_name='cleanness',
        ),
    ]
