# main/views.py
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from main.models import Product
from main.forms import ProductForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
import json
from django.contrib.auth.models import User



@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': 'Berguegou Briana Yadjam',
        'class': 'PBP KI',
        'npm': '2506561555',
        'application_name': 'Crampons Etoiles',
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect("main:show_main")
    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

def show_xml(request):
    data = Product.objects.all()
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

from django.http import JsonResponse
from .models import Product

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'rating': product.rating,
            'user_id': product.user.id if product.user else None,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)


def show_xml_by_id(request, id):
    try:
        news_item = Product.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", news_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        product = Product.objects.select_related('user').get(pk=id)
        product_data = {
            "id": str(product.id),
            "name": product.name,
            "category": product.category,
            "price": float(product.price),
            "description": product.description,
            "thumbnail": product.thumbnail.url if product.thumbnail else "",
            "is_featured": product.is_featured,
            "stock": product.stock,
            "rating": getattr(product, "rating", 0),
            "user_id": product.user.id if product.user else None,
            "created_at": product.created_at.isoformat() if product.created_at else None,
        }

        return JsonResponse(product_data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_main")
    return render(request, "edit_product.html", {"form": form, "product": product})

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    if request.method == "POST":
        product.delete()
        return redirect("main:show_main")
    

# === API (AJAX) layer ===

def _product_dict(p):
    return {
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "description": p.description,
        "thumbnail": p.thumbnail,
        "category": p.category,
        "is_featured": p.is_featured,
        "stock": p.stock,
        "rating": p.rating,
        "user_id": p.user.id if p.user else None,
    }

@require_http_methods(["GET", "POST"])
def api_products(request):
    if request.method == "GET":
        qs = Product.objects.all().order_by("-id")
        data = [_product_dict(p) for p in qs]
        return JsonResponse({"ok": True, "data": data})

    # POST create (must be authenticated)
    if not request.user.is_authenticated:
        return JsonResponse({"ok": False, "error": "Auth required"}, status=401)
    try:
        payload = json.loads(request.body or "{}")
        p = Product.objects.create(
            name=payload.get("name", ""),
            price=int(payload.get("price", 0)),
            description=payload.get("description", ""),
            thumbnail=payload.get("thumbnail", ""),
            category=payload.get("category", ""),
            is_featured=bool(payload.get("is_featured", False)),
            stock=int(payload.get("stock", 0)),
            rating=float(payload.get("rating", 0)),
            user=request.user,
        )
        return JsonResponse({"ok": True, "data": _product_dict(p)}, status=201)
    except Exception as e:
        return JsonResponse({"ok": False, "error": str(e)}, status=400)

@require_http_methods(["GET", "PATCH", "DELETE"])
def api_product_detail(request, pk):
    try:
        p = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"ok": False, "error": "Not found"}, status=404)

    if request.method == "GET":
        return JsonResponse({"ok": True, "data": _product_dict(p)})

    if not request.user.is_authenticated or p.user_id != request.user.id:
        return JsonResponse({"ok": False, "error": "Forbidden"}, status=403)

    if request.method == "PATCH":
        try:
            payload = json.loads(request.body or "{}")
            for field in ["name", "price", "description", "thumbnail", "category", "is_featured", "stock", "rating"]:
                if field in payload:
                    setattr(p, field, payload[field])
            p.save()
            return JsonResponse({"ok": True, "data": _product_dict(p)})
        except Exception as e:
            return JsonResponse({"ok": False, "error": str(e)}, status=400)

    # DELETE
    p.delete()
    return JsonResponse({"ok": True})

# === Auth API ===
@require_http_methods(["POST"])
def api_login(request):
    try:
        body = json.loads(request.body or "{}")
        user = authenticate(username=body.get("username"), password=body.get("password"))
        if user is None:
            return JsonResponse({"ok": False, "error": "Invalid credentials"}, status=400)
        login(request, user)
        response = JsonResponse({"ok": True, "username": user.username})
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    except Exception as e:
        return JsonResponse({"ok": False, "error": str(e)}, status=400)

@require_http_methods(["POST"])
def api_logout(request):
    logout(request)
    response = JsonResponse({"ok": True})
    response.delete_cookie('last_login')
    return response

@require_http_methods(["POST"])
def api_register(request):
    try:
        body = json.loads(request.body or "{}")
        username = body.get("username")
        password = body.get("password")
        if not username or not password:
            return JsonResponse({"ok": False, "error": "username and password required"}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({"ok": False, "error": "Username taken"}, status=400)
        u = User.objects.create_user(username=username, password=password)
        return JsonResponse({"ok": True, "username": u.username}, status=201)
    except Exception as e:
        return JsonResponse({"ok": False, "error": str(e)}, status=400)
