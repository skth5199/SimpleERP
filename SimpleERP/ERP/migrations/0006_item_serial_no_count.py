# Generated by Django 2.0 on 2018-04-16 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0005_serial_no_serial_no_tracking_stock_stock_tracking_stockentry_stockentry_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='serial_no_count',
            field=models.IntegerField(default=0),
        ),
    ]
