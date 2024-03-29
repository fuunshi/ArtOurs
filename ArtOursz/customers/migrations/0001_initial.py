# Generated by Django 5.0.1 on 2024-01-27 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0003_artistprofile_is_available_for_commission_and_more'),
        ('custom_auth', '0003_customuser_first_name_customuser_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='custom_auth.customuser')),
                ('bio', models.TextField(blank=True)),
                ('wishlist', models.ManyToManyField(blank=True, related_name='wishlisted_customers', to='artists.artwork')),
            ],
        ),
    ]
