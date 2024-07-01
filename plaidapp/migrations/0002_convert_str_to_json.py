# Generated by Django 5.0 on 2024-07-01 23:44

from django.db import migrations
import json


def convert_str_to_json(apps, schema_editor):
    PlaidTransaction = apps.get_model("plaidapp", "PlaidTransaction")
    for transaction in PlaidTransaction.objects.all():
        try:
            # convert the string to a list
            category_list = eval(transaction.category)
            transaction.category = json.dumps(category_list)
            transaction.save()
        except Exception as e:
            print(f"Error converting category for transaction {transaction.id}: {e}")
            continue


class Migration(migrations.Migration):
    """
    This migration aims to fix all PlaiTransaction category fields that are
    currently stored as strings. This migration will convert the string
    categories to JSON objects (arrays).
    """

    dependencies = [
        ("plaidapp", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(convert_str_to_json),
    ]
