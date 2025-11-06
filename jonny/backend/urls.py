from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("blog/", views.blog, name="blog"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    path("category/<slug:slug>/", views.category_view, name="category"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("wishlist/add/<slug:slug>/", views.wishlist_add, name="wishlist_add"),
    path("cart/add/<slug:slug>/", views.cart_add, name="cart_add"),
    path("cart/", views.cart_view, name="cart"),
    path("checkout/", views.simple_page, {"title": "Checkout"}, name="checkout"),
    path("coming-soon/", views.simple_page, {"title": "Coming Soon"}, name="coming_soon"),
    path("error/", views.simple_page, {"title": "Error"}, name="error"),
    path("faqs/", views.simple_page, {"title": "FAQs"}, name="faqs"),
    path("account/", views.simple_page, {"title": "My Account"}, name="account"),
    path("order-tracking/", views.simple_page, {"title": "Order Tracking"}, name="order_tracking"),
    path("wishlist/", views.simple_page, {"title": "Wishlist"}, name="wishlist"),
]
