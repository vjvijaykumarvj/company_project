# Generated by Django 4.0 on 2022-07-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, unique=True)),
                ('lastname', models.CharField(max_length=50, unique=True)),
                ('city', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=1000)),
                ('write_some', models.TextField(max_length=2000)),
            ],
        ),
    ]
