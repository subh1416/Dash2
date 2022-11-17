# Generated by Django 3.2.15 on 2022-10-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dash', '0009_auto_20221006_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graphs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperature', models.IntegerField(verbose_name='Temperature')),
                ('Time', models.IntegerField(verbose_name='Time')),
            ],
        ),
        migrations.DeleteModel(
            name='Graph',
        ),
    ]