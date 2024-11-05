# Generated by Django 5.1.2 on 2024-11-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0003_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='log',
            index=models.Index(fields=['customer_id'], name='logapp_log_custome_4c4be1_idx'),
        ),
        migrations.AddIndex(
            model_name='log',
            index=models.Index(fields=['time_stamp'], name='logapp_log_time_st_ebfb0b_idx'),
        ),
        migrations.AddIndex(
            model_name='log',
            index=models.Index(fields=['customer_id', 'time_stamp'], name='logapp_log_custome_c0ea2c_idx'),
        ),
    ]