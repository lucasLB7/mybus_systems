# Generated by Django 2.0.7 on 2018-07-04 07:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180703_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='laminateflooring',
            name='date_of_arrival',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]