# Generated by Django 3.2.18 on 2023-03-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0010_auto_20230323_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanic',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
