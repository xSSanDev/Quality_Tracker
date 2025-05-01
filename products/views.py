from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Product
from .forms import ProductForm
import csv
from django.utils import timezone
import datetime


def product_list(request):
    # Get search query and filter parameters
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    sort_by = request.GET.get('sort', '-created_at')  # Default: newest first

    # Start with all products
    products = Product.objects.all()

    # Apply search filter if provided
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__icontains=search_query)  # Added search by category
        )

    # Apply category filter if provided
    if category_filter and category_filter != 'All Categories':
        products = products.filter(category=category_filter)

    # Apply sorting
    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    elif sort_by == 'name':
        products = products.order_by('name')
    else:  # Default to newest
        products = products.order_by('-created_at')

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 10)  # Show 10 products per page

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    # Get category choices for the dropdown filter
    # Using the CATEGORY_CHOICES from the model instead of querying the database
    categories = Product.CATEGORY_CHOICES

    # Get stats for dashboard cards
    total_products = Product.objects.count()
    total_categories = len(categories)  # Use the length of CATEGORY_CHOICES

    # Count products created in the current month
    now = timezone.now()
    month_start = datetime.datetime(now.year, now.month, 1, tzinfo=now.tzinfo)
    new_this_month = Product.objects.filter(created_at__gte=month_start).count()

    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter,
        'sort_by': sort_by,
        'total_products': total_products,
        'total_categories': total_categories,
        'new_this_month': new_this_month,
    }

    return render(request, 'products/product_list.html', context)


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Product "{product.name}" was successfully added!')
            return redirect('product_list')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form.')
    else:
        form = ProductForm()

    return render(request, 'products/product_add.html', {'form': form})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_view.html', {'product': product})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Product "{product.name}" was successfully updated!')
            return redirect('product_list')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form.')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/product_edit.html', {'form': form, 'product': product})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'Product "{product_name}" was successfully deleted!')
        return redirect('product_list')

    return render(request, 'products/product_delete.html', {'product': product})


def export_products_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Category', 'Price', 'Description', 'Created At'])

    # Get filtered products if there are filters applied
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')

    products = Product.objects.all()

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__icontains=search_query)  # Added search by category
        )

    if category_filter and category_filter != 'All Categories':
        products = products.filter(category=category_filter)

    for product in products:
        writer.writerow([
            product.id,
            product.name,
            product.category,
            product.price,
            product.description,
            product.created_at.strftime('%Y-%m-%d %H:%M:%S')
        ])

    return response