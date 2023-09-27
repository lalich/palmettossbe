# Generated by Django 4.2.5 on 2023-09-26 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=101)),
                ('school_photo', models.ImageField(upload_to='')),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.IntegerField()),
                ('security_description', models.CharField(verbose_name=300)),
            ],
            options={
                'verbose_name_plural': 'schools',
            },
        ),
        migrations.CreateModel(
            name='SSS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('sss_photo', models.ImageField(upload_to='')),
                ('years_experience', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('specialty', models.CharField(max_length=101)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'ssss',
            },
        ),
    ]
