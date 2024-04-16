# Generated by Django 4.2.5 on 2024-02-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_customerinquiry_delete_customerinquire'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountName', models.TextField()),
                ('password', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('birthDate', models.DateField()),
                ('localArea', models.TextField()),
            ],
        ),
    ]
