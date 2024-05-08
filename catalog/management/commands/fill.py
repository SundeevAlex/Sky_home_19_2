import json

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('data.json', encoding='utf-8') as json_file:
            return json.load(json_file)

    @staticmethod
    def json_read_products():
        with open('data.json', encoding='utf-8') as json_file:
            return json.load(json_file)

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_create = []
        product_for_create = []
        for category in Command.json_read_categories():
            if category["model"] == "catalog.category":
                category_for_create.append(
                    Category(
                        id=category["pk"],
                        name=category["fields"]["name"],
                        description=category["fields"]["description"],
                    )
                )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            if product["model"] == "catalog.product":
                product_for_create.append(
                    Product(
                        id=product["pk"],
                        created_at=product["fields"]["created_at"],
                        name=product["fields"]["name"],
                        description=product["fields"]["description"],
                        image=product["fields"]["image"],
                        category=Category.objects.get(
                            pk=product["fields"]["category"]
                        ),
                        price=product["fields"]["price"],
                        updated_at=product["fields"]["updated_at"],
                    ),
                )

        Product.objects.bulk_create(product_for_create)
