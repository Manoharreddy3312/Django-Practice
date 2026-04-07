from datetime import datetime, timedelta
from decimal import Decimal
from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category


# Temporary catalog for UI/templates right now.
# After migrations + seed, we will switch cart/category pages to real database Products.
DUMMY_CATEGORIES = [
    ("mobiles", "Mobiles"),
    ("laptops", "Laptops"),
    ("mixi", "Mixi"),
    ("fan", "Fan"),
    ("cooler", "Cooler"),
    ("fridge", "Fridge"),
]

DUMMY_FASHION_CATEGORIES = [
    ("mens", "Mens Wear"),
    ("womens", "Womens Wear"),
]

DUMMY_PRODUCTS_BY_CATEGORY = {
    "mobiles": [
        {"id": 1, "name": "Smartphone A1", "price": Decimal("6999.00")},
        {"id": 2, "name": "Smartphone B2", "price": Decimal("8999.00")},
        {"id": 3, "name": "Smartphone C3", "price": Decimal("12999.00")},
    ],
    "laptops": [
        {"id": 4, "name": "Laptop 14\" i3", "price": Decimal("28999.00")},
        {"id": 5, "name": "Laptop 15\" i5", "price": Decimal("38999.00")},
    ],
    "mixi": [
        {"id": 6, "name": "Mixi 500W", "price": Decimal("2499.00")},
        {"id": 7, "name": "Mixi 750W", "price": Decimal("3499.00")},
    ],
    "fan": [
        {"id": 8, "name": "Table Fan 12\"", "price": Decimal("1299.00")},
        {"id": 9, "name": "Ceiling Fan 48\"", "price": Decimal("2399.00")},
    ],
    "cooler": [
        {"id": 10, "name": "Air Cooler 25L", "price": Decimal("7999.00")},
        {"id": 11, "name": "Air Cooler 35L", "price": Decimal("9999.00")},
    ],
    "fridge": [
        {"id": 12, "name": "Single Door 165L", "price": Decimal("17999.00")},
        {"id": 13, "name": "Double Door 250L", "price": Decimal("27999.00")},
    ],
    "mens": [
        {"id": 101, "name": "Men T-Shirt", "price": Decimal("699.00")},
        {"id": 102, "name": "Men Formal Shirt", "price": Decimal("1199.00")},
    ],
    "womens": [
        {"id": 201, "name": "Women Kurti", "price": Decimal("999.00")},
        {"id": 202, "name": "Women Jeans", "price": Decimal("1299.00")},
    ],
}


def _dummy_get_product(product_id: int) -> dict[str, Any] | None:
    for items in DUMMY_PRODUCTS_BY_CATEGORY.values():
        for p in items:
            if p["id"] == product_id:
                return p
    return None


def _get_cart_from_session(request: HttpRequest) -> dict[str, int]:
    cart = request.session.get("cart", {})
    if not isinstance(cart, dict):
        return {}
    # Normalize values to int
    normalized: dict[str, int] = {}
    for k, v in cart.items():
        try:
            normalized[str(k)] = int(v)
        except (TypeError, ValueError):
            continue
    return normalized


def _save_cart_to_session(request: HttpRequest, cart: dict[str, int]) -> None:
    request.session["cart"] = cart
    request.session.modified = True


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "app/home.html",
        {
            "electronics_categories": DUMMY_CATEGORIES,
            "fashion_categories": DUMMY_FASHION_CATEGORIES,
        },
    )


def register_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect("home")
        messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, "app/register.html", {"form": form})


def login_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            next_url = request.GET.get("next")
            return redirect(next_url or "home")
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm(request)
    return render(request, "app/login.html", {"form": form})


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.success(request, "Logged out.")
    return redirect("home")


def search_products(request: HttpRequest) -> HttpResponse:
    q = (request.GET.get("q") or "").strip()
    products = Product.objects.filter(is_active=True).select_related("category")
    if q:
        products = products.filter(
            Q(name__icontains=q)
            | Q(description__icontains=q)
            | Q(category__name__icontains=q)
        )
    products = products.order_by("-created_at")[:60]
    return render(request, "app/search.html", {"q": q, "products": products})


def electronics(request: HttpRequest) -> HttpResponse:
    return render(request, "app/electronics.html", {"categories": DUMMY_CATEGORIES})


def electronics_category(request: HttpRequest, slug: str) -> HttpResponse:
    category_name = dict(DUMMY_CATEGORIES).get(slug, slug)
    products = DUMMY_PRODUCTS_BY_CATEGORY.get(slug, [])
    return render(
        request,
        "app/category.html",
        {"category_type": "electronics", "category_slug": slug, "category_name": category_name, "products": products},
    )


def fashion(request: HttpRequest) -> HttpResponse:
    return render(request, "app/fashion.html", {"categories": DUMMY_FASHION_CATEGORIES})


def fashion_category(request: HttpRequest, slug: str) -> HttpResponse:
    category_name = dict(DUMMY_FASHION_CATEGORIES).get(slug, slug)
    products = DUMMY_PRODUCTS_BY_CATEGORY.get(slug, [])
    return render(
        request,
        "app/category.html",
        {"category_type": "fashion", "category_slug": slug, "category_name": category_name, "products": products},
    )


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "app/about.html")


def cart_view(request: HttpRequest) -> HttpResponse:
    cart = _get_cart_from_session(request)
    cart_items: list[dict[str, Any]] = []
    total = Decimal("0.00")
    for pid_str, qty in cart.items():
        try:
            pid = int(pid_str)
        except ValueError:
            continue
        product = _dummy_get_product(pid)
        if not product:
            continue
        unit = product["price"]
        subtotal = unit * qty
        total += subtotal
        cart_items.append(
            {
                "product_id": pid,
                "name": product["name"],
                "unit_price": unit,
                "quantity": qty,
                "subtotal": subtotal,
            }
        )

    return render(request, "app/cart.html", {"cart_items": cart_items, "cart_total": total})


def cart_add(request: HttpRequest, product_id: int) -> HttpResponse:
    cart = _get_cart_from_session(request)
    pid = str(product_id)
    cart[pid] = cart.get(pid, 0) + 1
    _save_cart_to_session(request, cart)
    return HttpResponseRedirect("/cart/")


def cart_increment(request: HttpRequest, product_id: int) -> HttpResponse:
    return cart_add(request, product_id)


def cart_decrement(request: HttpRequest, product_id: int) -> HttpResponse:
    cart = _get_cart_from_session(request)
    pid = str(product_id)
    if pid in cart:
        cart[pid] -= 1
        if cart[pid] <= 0:
            cart.pop(pid, None)
    _save_cart_to_session(request, cart)
    return HttpResponseRedirect("/cart/")


def cart_remove(request: HttpRequest, product_id: int) -> HttpResponse:
    cart = _get_cart_from_session(request)
    cart.pop(str(product_id), None)
    _save_cart_to_session(request, cart)
    return HttpResponseRedirect("/cart/")


def checkout(request: HttpRequest) -> HttpResponse:
    # Real auth + order placement will come next.
    cart = _get_cart_from_session(request)
    cart_items: list[dict[str, Any]] = []
    total = Decimal("0.00")
    for pid_str, qty in cart.items():
        try:
            pid = int(pid_str)
        except ValueError:
            continue
        product = _dummy_get_product(pid)
        if not product:
            continue
        unit = product["price"]
        subtotal = unit * qty
        total += subtotal
        cart_items.append(
            {
                "product_id": pid,
                "name": product["name"],
                "unit_price": unit,
                "quantity": qty,
                "subtotal": subtotal,
            }
        )

    return render(
        request,
        "app/checkout.html",
        {"cart_items": cart_items, "cart_total": total, "dummy_user_required_auth": True},
    )


def razorpay_create_order(request: HttpRequest) -> HttpResponse:
    # Placeholder endpoint for UI flow. Next step will integrate Razorpay properly.
    return HttpResponseRedirect("/orders/1/tracking/")


def razorpay_success(request: HttpRequest) -> HttpResponse:
    return HttpResponseRedirect("/orders/1/tracking/")


def razorpay_failed(request: HttpRequest) -> HttpResponse:
    return HttpResponseRedirect("/checkout/")


def order_tracking(request: HttpRequest, order_id: int) -> HttpResponse:
    # Placeholder tracking timings (72 hours total).
    now = timezone.now()
    created_at = now - timedelta(hours=3)  # demo: show around first segment
    return render(
        request,
        "app/tracking.html",
        {
            "order_id": order_id,
            "order_created_at_iso": created_at.isoformat(),
        },
    )
