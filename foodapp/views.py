from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import FoodForm
from .models import Food, Cart
from django.contrib import messages, auth
# Create your views here.


class LoginView(View):

    def get(self, request):
        context = {'error': None}
        return render(request, 'login.html', context=context)

    def post(self, request):
        data = request.POST
        user = authenticate(email=data['email'], password=data['password'])
        if user is None:
            messages.warning(request, "Email or Password is invalid")
            context = {'error': 'Email or password is Invalid'}
            return render(request, 'login.html', context=context)
        elif user.is_superuser:
            login(request, user)
            url = reverse('admin_side:admin-dashboard')
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, "You have not permission to login in admin penal")
            context = {'error': 'Email or password is Invalid'}
            return render(request, 'login.html', context=context)


class AdminDashboardView(View):

    def get(self, request):
        message = request.GET.get('message', None)
        food_items = Food.objects.all()
        confirm_items = Cart.objects.filter(is_confirm=True)
        form = FoodForm()

        return render(
            request,
            'admin-dashboard.html',
            context={
                'foods': food_items,
                'confirm_items': confirm_items,
                'form': form,
                'message': message
            }
        )


class CreateFoodView(View):

    def post(self, request):
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        url = reverse('food_app:admin-dashboard')
        url += "?message=Item-Created-Successfully/"
        return HttpResponseRedirect(url)



class UpdateDelteFoodView(View):

    def get(self, request, id):
        food_obj = Food.objects.get(id=id)
        food_obj.delete()
        url = reverse('food_app:admin-dashboard')
        url += "?message=Item-Deleted-Successfully/"
        return HttpResponseRedirect(url)

    def post(self, request, id):
        instance = Food.objects.get(id=id)
        form = FoodForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
        url = reverse('food_app:admin-dashboard')
        url += "?message=Item-Updated-Successfully/"
        return HttpResponseRedirect(url)


class MainView(View):

    def get(self, request):
        message = request.GET.get('message', None)
        return render(request, 'project.html',  context={'message': message})


class ServicesView(View):

    def get(self, request):
        return render(request, 'services.html')


class MainMenuView(View):

    def get(self, request):
        message = request.GET.get('message', None)
        food_objects = Food.objects.all()
        return render(
            request, 'menu.html',
            context={
                'foods': food_objects,
                'message': message
            }
        )


class AddOrderView(View):

    def get(self, request):
        message = request.GET.get('message', None)
        cart = Cart.objects.filter(is_confirm= False)
        price_sum = 0
        for food in cart:
            food_obj = Food.objects.get(id=food.food.id)
            price_sum += food_obj.price

        return render(
            request, 'addorder.html',
            context={
                'cart_item': cart,
                'price_sum': price_sum,
                'message': message
            }
        )


class CartItemView(View):

    def get(self, request, id):
        food_obj = Food.objects.get(id=id)
        cart_obj = Cart(food=food_obj)
        cart_obj.save()
        url = reverse('food_app:menu-page')
        url += "?message=Added-Cart-Successfully/"
        return HttpResponseRedirect(url)

    def post(self, request, id):
        cart = Cart.objects.get(id=id)
        cart.delete()
        url = reverse('food_app:order-page')
        url += "?message=Item-Deleted-Successfully/"
        return HttpResponseRedirect(url)


class ConfirmOrderView(View):

    def get(self, request):
        cart = Cart.objects.all()

        for item in cart:
            item.is_confirm = True
            item.save()

        url = reverse('food_app:main-page')
        url += "?message=Order-Confirmed/"
        return HttpResponseRedirect(url)



class ContactView(View):

    def get(self, request):
        message = request.GET.get('message', None)

        return render(request, 'contact.html', context={'message': message})

    def post(self, request):
        url = reverse('food_app:contact-page')
        url += "?message=request_submited/"
        return HttpResponseRedirect(url)
