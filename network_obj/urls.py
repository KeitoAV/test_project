from django.urls import path

from network_obj import views


urlpatterns = [
    path('object/create', views.NetworkObjectCreateView.as_view(), name='object_create'),
    path('object/list', views.NetworkObjectListView.as_view(), name='object_list'),
    path('object/<pk>', views.NetworkObjectView.as_view(), name='object_pk'),


    path('product/create', views.ProductCreateView.as_view(), name='product_create'),
    path('product/list', views.ProductListView.as_view(), name='product_list'),
    path('product/<pk>', views.ProductView.as_view(), name='product_pk'),

]
