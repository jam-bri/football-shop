from django.urls import path
from main.views import show_main, create_product, product_detail, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product,api_products, api_product_detail, api_login, api_logout, api_register

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('products/add/', create_product, name='create_product'),
    path('products/<str:id>/', product_detail, name='product_detail'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<int:id>/', edit_product, name='edit_product'),
    path('delete-product/<int:id>/', delete_product, name='delete_product'),
        # === NEW: API endpoints for AJAX ===
    path('api/products/', api_products, name='api_products'),                 # GET list, POST create
    path('api/products/<int:pk>/', api_product_detail, name='api_product'),   # GET detail, PATCH/DELETE
    path('api/auth/login/', api_login, name='api_login'),
    path('api/auth/logout/', api_logout, name='api_logout'),
    path('api/auth/register/', api_register, name='api_register'),
    
]