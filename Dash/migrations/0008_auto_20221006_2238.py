# Generated by Django 3.2.15 on 2022-10-06 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dash', '0007_auto_20221006_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graphs',
            old_name='Temperature1',
            new_name='Temperature',
        ),
        migrations.RenameField(
            model_name='graphs',
            old_name='Time2',
            new_name='Time',
        ),
    ]
