# Generated by Django 2.2 on 2019-06-30 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20190630_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crystal',
            old_name='lore',
            new_name='lores',
        ),
    ]
