# Generated by Django 4.2.3 on 2023-07-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.IntegerField()),
                ('empname', models.CharField(max_length=225)),
                ('empsalary', models.IntegerField()),
                ('empaddress', models.CharField(max_length=225)),
            ],
        ),
    ]