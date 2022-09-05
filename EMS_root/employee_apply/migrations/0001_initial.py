# Generated by Django 4.0 on 2022-07-29 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_reg', '0004_alter_contact_address_alter_employee_model_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_reg.employee_model')),
            ],
        ),
    ]