# Generated by Django 4.2.6 on 2023-10-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='footballplayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
                ('experience', models.CharField(max_length=10)),
            ],
        ),
    ]
