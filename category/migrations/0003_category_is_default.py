# Generated by Django 5.0 on 2023-12-24 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
