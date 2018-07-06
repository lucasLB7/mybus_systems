# Generated by Django 2.0.7 on 2018-07-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_laminateflooring_date_of_arrival'),
    ]

    operations = [
        migrations.AddField(
            model_name='laminateflooring',
            name='purchase_cost',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='laminateflooring',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='laminateflooring',
            name='sales_cost',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
