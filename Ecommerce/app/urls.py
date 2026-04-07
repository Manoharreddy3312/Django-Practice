from django.urls import path
from .views import (
    about,
    cart_add,
    cart_decrement,
    cart_increment,
    cart_remove,
    cart_view,
    checkout,
    electronics,
    electronics_category,
    fashion,
    fashion_category,
    home,
    login_view,
    logout_view,
    order_tracking,
    razorpay_create_order,
    razorpay_failed,
    razorpay_success,
    register_view,
    search_products,
)

urlpatterns = [
    path("", home, name="home"),
    path("search/", search_products, name="search"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("electronics/", electronics, name="electronics"),
    path("electronics/<slug:slug>/", electronics_category, name="electronics_category"),
    path("fashion/", fashion, name="fashion"),
    path("fashion/<slug:slug>/", fashion_category, name="fashion_category"),
    path("about/", about, name="about"),

    path("cart/", cart_view, name="cart"),
    path("cart/add/<int:product_id>/", cart_add, name="cart_add"),
    path("cart/increment/<int:product_id>/", cart_increment, name="cart_increment"),
    path("cart/decrement/<int:product_id>/", cart_decrement, name="cart_decrement"),
    path("cart/remove/<int:product_id>/", cart_remove, name="cart_remove"),

    path("checkout/", checkout, name="checkout"),

    # Razorpay payment flow (placeholder endpoints for now)
    path("pay/razorpay/create/", razorpay_create_order, name="razorpay_create_order"),
    path("pay/razorpay/success/", razorpay_success, name="razorpay_success"),
    path("pay/razorpay/failed/", razorpay_failed, name="razorpay_failed"),

    path("orders/<int:order_id>/tracking/", order_tracking, name="order_tracking"),
]

