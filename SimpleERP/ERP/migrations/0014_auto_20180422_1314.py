# Generated by Django 2.0 on 2018-04-22 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0013_auto_20180422_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='tax_amount',
            new_name='buying_tax_amount',
        ),
        migrations.RenameField(
            model_name='pricelog',
            old_name='tax_amount',
            new_name='buying_tax_amount',
        ),
        migrations.RemoveField(
            model_name='price',
            name='tax_group',
        ),
        migrations.RemoveField(
            model_name='pricelog',
            name='tax_group',
        ),
        migrations.AddField(
            model_name='price',
            name='buying_tax_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Price_buying_tax_group', to='ERP.TaxGroup'),
        ),
        migrations.AddField(
            model_name='price',
            name='selling_tax_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='price',
            name='selling_tax_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Price_selling_tax_group', to='ERP.TaxGroup'),
        ),
        migrations.AddField(
            model_name='pricelog',
            name='buying_tax_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='PriceLog_buying_tax_group', to='ERP.TaxGroup'),
        ),
        migrations.AddField(
            model_name='pricelog',
            name='selling_tax_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pricelog',
            name='selling_tax_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='PriceLog_selling_tax_group', to='ERP.TaxGroup'),
        ),
    ]
