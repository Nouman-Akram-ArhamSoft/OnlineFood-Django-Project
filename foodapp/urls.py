from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'food_app'

urlpatterns = [
    path('', views.MainView.as_view(), name='main-page'),
    path('services/', views.ServicesView.as_view(), name='services-page'),
    path('menu/', views.MainMenuView.as_view(), name='menu-page'),
    path('add-order/', views.AddOrderView.as_view(), name='order-page'),
    path('cart-items/<int:id>/', views.CartItemView.as_view(), name='cart-items'),
    path('confirm-order/', views.ConfirmOrderView.as_view(), name='confirm-order'),
    path('confirm-order/', views.ConfirmOrderView.as_view(), name='confirm-order'),
    path('admin-login/', views.LoginView.as_view(), name='admin-login'),
    path('admin-dashboard/', views.AdminDashboardView.as_view(), name='admin-dashboard'),
    path('create-food/', views.CreateFoodView.as_view(), name='create-food'),
    path('update&delete-food/<int:id>/', views.UpdateDelteFoodView.as_view(), name='update-delete-food'),
    path('contact/', views.ContactView.as_view(), name='contact-page'),

]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
