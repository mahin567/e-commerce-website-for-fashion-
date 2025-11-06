from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Category, Product

def home(request):
    categories = Category.objects.all()
    new_collections = Product.objects.filter(is_new=True)[:6]
    new_arrivals = Product.objects.order_by("-created_at")[:10]
    # pick 3 featured categories (or fewer if not enough)
    featured_categories = Category.objects.all()[:3]

    # sample session cart math (dummy)
    cart = request.session.get("cart", {})
    products_in_cart = Product.objects.filter(slug__in=cart.keys()) if cart else []
    cart_total = sum(float(p.price) * cart.get(p.slug, 0) for p in products_in_cart)
    request.session["cart_total"] = round(cart_total, 2)

    ctx = {
        "categories": categories,
        "new_collections": new_collections,
        "new_arrivals": new_arrivals,
        "featured_categories": featured_categories,
    }
    return render(request, "home.html", ctx)


def shop(request):
    products = Product.objects.all()
    return render(request, "simple_list.html", {"title": "Shop", "products": products})


def blog(request):
    return render(request, "simple_page.html", {"title": "Blog"})


def about(request):
    return render(request, "simple_page.html", {"title": "About"})


def contact(request):
    return render(request, "simple_page.html", {"title": "Contact"})


def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, "simple_list.html", {"title": category.name, "products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "simple_detail.html", {"product": product})


def search(request):
    q = request.GET.get("q", "")
    products = Product.objects.filter(
        Q(name__icontains=q) | Q(description__icontains=q) | Q(category__name__icontains=q)
    ) if q else Product.objects.none()
    return render(request, "simple_list.html", {"title": f"Search: {q}", "products": products})


# --- wishlist & cart (very simple session stubs) ---

def wishlist_add(request, slug):
    wl = set(request.session.get("wishlist", []))
    wl.add(slug)
    request.session["wishlist"] = list(wl)
    return redirect("product_detail", slug=slug)


def cart_add(request, slug):
    cart = request.session.get("cart", {})
    cart[slug] = cart.get(slug, 0) + 1
    request.session["cart"] = cart
    return redirect("product_detail", slug=slug)


# --- simple placeholders for named URLs used in template ---

def simple_page(request, title):
    return render(request, "simple_page.html", {"title": title})


def cart_view(request):
    cart = request.session.get("cart", {})
    products = Product.objects.filter(slug__in=cart.keys())
    items = []
    total = 0
    for p in products:
        qty = cart.get(p.slug, 0)
        line = {"product": p, "qty": qty, "line_total": float(p.price) * qty}
        items.append(line)
        total += line["line_total"]
    request.session["cart_total"] = round(total, 2)
    return render(request, "cart.html", {"items": items, "total": total})
