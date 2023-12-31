# Generated by Django 4.2.7 on 2023-11-21 10:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="rate",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=3,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="rate",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=3,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
    ]
