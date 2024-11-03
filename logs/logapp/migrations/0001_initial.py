# Generated by Django 5.1.2 on 2024-11-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField()),
                ('customer_id', models.CharField(max_length=255)),
                ('request_path', models.CharField(max_length=255)),
                ('status_code', models.IntegerField()),
                ('duration', models.FloatField()),
            ],
        ),
    ]