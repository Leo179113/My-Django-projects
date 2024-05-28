from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ProductForm
from .models import Product, CartItem
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def product_list(request):
    query = request.GET.get('q', '')
    fruits = Product.objects.filter(category='Fruits')
    vegetables = Product.objects.filter(category='Vegetables')
    farm_animals = Product.objects.filter(category='Farm Animals')

    if query:
        fruits = fruits.filter(name__icontains=query)
        vegetables = vegetables.filter(name__icontains=query)
        farm_animals = farm_animals.filter(name__icontains=query)

    context = {
        'fruits': fruits,
        'vegetables': vegetables,
        'farm_animals': farm_animals,
    }
    return render(request, 'product_list.html', context)

def add_to_cart(request, product_id, product_name, product_price):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.name = product_name
    cart_item.price = product_price
    cart_item.save()
    return redirect('cart:view_cart')

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def search_results(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query) if query else Product.objects.all()
    return render(request, 'search_results.html', {'products': products, 'query': query})


def search_products(request):
    query = request.GET.get('query')
    products = Product.objects.filter(name__icontains=query, available=True)
    return render(request, 'product_list.html', {'products': products})



