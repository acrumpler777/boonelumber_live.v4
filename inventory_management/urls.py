from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.inventory_main, name="inventory_main"),
    path('update_inventory/', views.update_inventory, name='inventory_management'),
    path('update_inventory/purchase_order/', views.purchase_order_func, name='purchase_order'),
    path('update_inventory/inventory_adjustment/', views.inventory_adjustment, name='inventory_adjustment'),
    path('update_inventory/update_inventory_item/<str:pk>/', views.update_inventory, name='update_inventory'),

    path('update_inventory/sales_order/', views.sales_order, name='sales_order'),



    path('analyze_inventory/', views.analyze_inventory, name="analyze_inventory"),

    path('view_inventory_All/', views.view_inventory_All, name="view_inventory_All"),
    path('view_inventory_401_WRC/', views.view_inventory_401_WRC, name="view_inventory_401_WRC"),
    path('view_inventory_CandBTR/', views.view_inventory_CandBTR, name="view_inventory_CandBTR"),
    path('view_inventory_AYC/', views.view_inventory_AYC, name="view_inventory_AYC"),
    path('view_inventory_Cypress/', views.view_inventory_Cypress, name="view_inventory_Cypress"),
    path('view_inventory_D_FIR/', views.view_inventory_D_FIR, name="view_inventory_D_FIR"),
    path('view_inventory_EWP/', views.view_inventory_EWP, name="view_inventory_EWP"),
    path('view_inventory_Oak/', views.view_inventory_Oak, name="view_inventory_Oak"),
    path('view_inventory_Spruce/', views.view_inventory_Spruce, name="view_inventory_Spruce"),
    path('view_inventory_WRC/', views.view_inventory_WRC, name="view_inventory_WRC"),
    path('export/csv/', views.export_users_csv, name='export_users_csv'),

]