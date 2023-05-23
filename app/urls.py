from django.urls import path
from app import views

urlpatterns = [
    # login
    path('',views.loginn),
    path('login_post/',views.login_post),
    # logout
    path('logout/',views.logout),
    # register
    path('register/',views.register),
    path('register_post/',views.register_post),
    # UserHome
    path('user_home/',views.user_home),
    # adminhome
    path('admin_home/',views.admin_home),
    # additem
    path('admin_add_item/',views.admin_add_item),
    path('admin_add_item_post/',views.admin_add_item_post),
    # deletproduct
    path('admin_delete_product/<str:pid>',views.admin_delete_product),
    # editproduct
    path('admin_edit_product/<str:pid>',views.admin_edit_item),
    path('admin_edit_product_post/',views.admin_edit_item_post),
    # viewproduct
    path('admin_view_product/',views.admin_view_product),
    # addcart
    path('user_add_cart/<str:pid>',views.user_add_cart),
    path('user_add_cart_post/',views.user_add_cart_post),
    # userviewproduct
    path('user_view_product/',views.user_view_product),
    # viewcart
    path('user_view_cart/',views.user_view_cart),
    # deletecart
    path('user_delete_cart/<str:cid>',views.user_delete_cart),

    path('styled/',views.styled),
    path('admin_styled/',views.admin_styled)
]