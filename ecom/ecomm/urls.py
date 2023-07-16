from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path(
        '/store/place_order',
        views.store,
        {'place_order': True},
        name="place_order"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('accounts/', include('user_profile.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path(
        'product/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    )
]
