def shop_counts(request):
    """
    Very simple session-based counters so your template placeholders show values.
    You can replace with real cart/wishlist logic later.
    """
    cart = request.session.get("cart", {})
    wishlist = request.session.get("wishlist", set())

    # session serializer can’t store sets by default, normalize
    if isinstance(wishlist, list):
        wl_count = len(wishlist)
    else:
        wl_count = len(list(wishlist))

    cart_count = sum(cart.values()) if isinstance(cart, dict) else 0
    cart_total = request.session.get("cart_total", 0)

    return {
        "cart_count": cart_count,
        "wishlist_count": wl_count,
        "cart_total": cart_total,
    }
