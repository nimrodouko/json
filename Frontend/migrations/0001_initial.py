# Generated by Django 4.2 on 2023-09-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=20)),
                ('Surname', models.CharField(max_length=20)),
                ('Age', models.PositiveIntegerField()),
            ],
        ),
    ]
