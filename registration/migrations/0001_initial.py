# Generated by Django 5.1.3 on 2024-12-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
    ]
