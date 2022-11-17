# Generated by Django 3.2.15 on 2022-10-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dash', '0008_auto_20221006_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('Temperature', models.IntegerField(verbose_name='Temperature')),
                ('Time', models.IntegerField(verbose_name='Time')),
            ],
        ),
        migrations.DeleteModel(
            name='Graphs',
        ),
    ]