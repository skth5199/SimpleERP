# Generated by Django 2.0 on 2018-04-24 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0015_purchaseinvoice_purchaseinvoice_items_taxsplitup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='primary_contact_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]