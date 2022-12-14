# Generated by Django 4.0 on 2022-07-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_reg', '0002_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, unique=True)),
                ('lastname', models.CharField(max_length=50, unique=True)),
                ('city', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=30, unique=True)),
                ('c_password', models.CharField(max_length=30, unique=True)),
                ('username', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
