from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot-password/', views.password_reset_request, name='password_reset_request'),
    path('reset-password/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Transactions
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.transaction_add, name='transaction_add'),
    path('transactions/<int:pk>/edit/', views.transaction_edit, name='transaction_edit'),
    path('transactions/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),

    # AJAX
    path('ajax/categories/', views.get_categories, name='get_categories'),
    path('ajax/subcategories/', views.get_subcategories, name='get_subcategories'),

    # Calendar
    path('calendar/', views.calendar_view, name='calendar'),
    path('calendar/<int:year>/<int:month>/<int:day>/', views.calendar_day_detail, name='calendar_day'),

    # Reports
    path('reports/', views.reports, name='reports'),

    # Analytics
    path('analytics/', views.analytics, name='analytics'),

    # Categories
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/toggle/', views.category_toggle, name='category_toggle'),
    path('categories/sub/add/', views.subcategory_add, name='subcategory_add'),
    path('categories/sub/<int:pk>/edit/', views.subcategory_edit, name='subcategory_edit'),
]
# This line already exists — just ensure register is added
