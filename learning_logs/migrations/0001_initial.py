# Generated by Django 4.1.2 on 2022-10-05 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
