# main/views.py
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from main.models import Product
from main.forms import ProductForm

def show_main(request):
    products = Product.objects.all()
    context = {
        'name': 'Berguegou Briana Yadjam',
        'class': 'PBP KI',
        'npm': '2506561555',
        'application_name': 'Crampons Etoiles',
        'products': products,
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")
    context = {'form': form}
    return render(request, "create_product.html", context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

def show_xml(request):
    data = Product.objects.all()
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    json_data = serializers.serialize("json", data)
    return HttpResponse( json_data, content_type="application/json")

def show_xml_by_id(request, id):
    try:
        news_item = Product.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", news_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        news_item = Product.objects.get(pk=id)
        json_data = serializers.serialize("json", [news_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
