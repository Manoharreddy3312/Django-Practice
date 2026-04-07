from __future__ import annotations

import os
import urllib.request
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand

from app.models import Category, Product


@dataclass(frozen=True)
class SeedProduct:
    category_slug: str
    name: str
    price: Decimal
    image_url: str


ELECTRONICS = [
    ("mobiles", "Mobiles"),
    ("laptops", "Laptops"),
    ("mixi", "Mixi"),
    ("fan", "Fan"),
    ("cooler", "Cooler"),
    ("fridge", "Fridge"),
    ("tv", "TVs"),
    ("headphones", "Headphones"),
]

FASHION = [
    ("mens", "Mens Wear"),
    ("womens", "Womens Wear"),
    ("footwear", "Footwear"),
    ("watches", "Watches"),
]

SEED_PRODUCTS: list[SeedProduct] = [
    # Mobiles
    SeedProduct("mobiles", "Smartphone A1 (6GB/128GB)", Decimal("6999.00"), "https://picsum.photos/seed/mobile-a1/600/600"),
    SeedProduct("mobiles", "Smartphone B2 (8GB/128GB)", Decimal("8999.00"), "https://picsum.photos/seed/mobile-b2/600/600"),
    SeedProduct("mobiles", "Smartphone C3 (8GB/256GB)", Decimal("12999.00"), "https://picsum.photos/seed/mobile-c3/600/600"),
    # Laptops
    SeedProduct("laptops", "Laptop 14\" i3 • 8GB/256GB", Decimal("28999.00"), "https://picsum.photos/seed/laptop-14/600/600"),
    SeedProduct("laptops", "Laptop 15\" i5 • 16GB/512GB", Decimal("38999.00"), "https://picsum.photos/seed/laptop-15/600/600"),
    # Appliances
    SeedProduct("mixi", "Mixer Grinder 500W", Decimal("2499.00"), "https://picsum.photos/seed/mixi-500/600/600"),
    SeedProduct("fan", "Ceiling Fan 48\" (High Speed)", Decimal("2399.00"), "https://picsum.photos/seed/fan-48/600/600"),
    SeedProduct("cooler", "Air Cooler 35L (Honeycomb)", Decimal("9999.00"), "https://picsum.photos/seed/cooler-35/600/600"),
    SeedProduct("fridge", "Double Door Fridge 250L", Decimal("27999.00"), "https://picsum.photos/seed/fridge-250/600/600"),
    # TVs/Audio
    SeedProduct("tv", "43\" 4K Smart TV", Decimal("25999.00"), "https://picsum.photos/seed/tv-43/600/600"),
    SeedProduct("headphones", "Wireless Headphones (Noise Cancel)", Decimal("2999.00"), "https://picsum.photos/seed/headphones/600/600"),
    # Fashion
    SeedProduct("mens", "Men T-Shirt (Cotton)", Decimal("699.00"), "https://picsum.photos/seed/mens-tee/600/600"),
    SeedProduct("womens", "Women Kurti (Printed)", Decimal("999.00"), "https://picsum.photos/seed/womens-kurti/600/600"),
    SeedProduct("footwear", "Running Shoes", Decimal("1799.00"), "https://picsum.photos/seed/shoes/600/600"),
    SeedProduct("watches", "Analog Watch", Decimal("1499.00"), "https://picsum.photos/seed/watch/600/600"),
]


def _ensure_categories() -> None:
    electronics_root, _ = Category.objects.get_or_create(name="Electronics", parent=None, defaults={"sort_order": 1})
    fashion_root, _ = Category.objects.get_or_create(name="Fashion", parent=None, defaults={"sort_order": 2})

    for idx, (slug, name) in enumerate(ELECTRONICS, start=1):
        Category.objects.get_or_create(
            slug=slug,
            defaults={"name": name, "parent": electronics_root, "sort_order": idx},
        )
    for idx, (slug, name) in enumerate(FASHION, start=1):
        Category.objects.get_or_create(
            slug=slug,
            defaults={"name": name, "parent": fashion_root, "sort_order": idx},
        )


def _download_to_storage(url: str, storage_path: str) -> str:
    with urllib.request.urlopen(url, timeout=25) as resp:  # nosec - dev seed utility
        content = resp.read()
    default_storage.save(storage_path, ContentFile(content))
    return storage_path


class Command(BaseCommand):
    help = "Seed categories and sample products (downloads images)."

    def add_arguments(self, parser):
        parser.add_argument("--clear", action="store_true", help="Delete existing products before seeding.")
        parser.add_argument("--skip-images", action="store_true", help="Create products without downloading images.")

    def handle(self, *args, **options):
        clear: bool = options["clear"]
        skip_images: bool = options["skip_images"]

        _ensure_categories()

        if clear:
            Product.objects.all().delete()

        created = 0
        for sp in SEED_PRODUCTS:
            category = Category.objects.get(slug=sp.category_slug)
            product, is_new = Product.objects.get_or_create(
                name=sp.name,
                defaults={
                    "category": category,
                    "price": sp.price,
                    "description": "Seeded demo product.",
                    "is_active": True,
                },
            )
            if not is_new:
                continue

            if not skip_images:
                filename = f"seed_{product.id}.jpg"
                storage_path = str(Path("products") / filename).replace("\\", "/")
                try:
                    _download_to_storage(sp.image_url, storage_path)
                    product.image = storage_path
                    product.save(update_fields=["image"])
                except Exception as e:  # noqa: BLE001
                    self.stderr.write(self.style.WARNING(f"Image download failed for {product.name}: {e}"))

            created += 1

        self.stdout.write(self.style.SUCCESS(f"Seed complete. Created {created} products."))

