# Generated by Django 3.2 on 2021-04-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='dateOfJoin',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]