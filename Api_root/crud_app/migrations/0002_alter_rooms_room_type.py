# Generated by Django 4.0 on 2022-08-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='room_type',
            field=models.CharField(choices=[('AC', 'AC'), ('Non AC', 'Non AC'), ('King', 'King'), ('Primier', 'Premier')], default='AC', max_length=10),
        ),
    ]
