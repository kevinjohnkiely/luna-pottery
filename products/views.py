from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Rating
from .forms import RatingForm
from django.contrib.auth.models import User


def all_products(request):
    """A view to render the list of products page, including sorting & searching"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lowercase_name'
                products = products.annotate(lowercase_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, "You did not enter a search term!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'selected_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_single(request, product_id):
    """A view to render a single page showing the individual product details"""
    product = get_object_or_404(Product, pk=product_id)

    # if request.POST:
    #     user = request.user
    #     review_form = ReviewForm(data=request.POST)

    #     if review_form.is_valid():
    #         review = review_form.save(commit=False)
    #         review.product = product
    #         review.user = user
    #         review.save()
    #     else:
    #         review_form = ReviewForm()

    queryset = Rating.objects.filter(product=product_id)

    total_ratings = 0
    for result in queryset:
        total_ratings += result.rating

    avg_rating = total_ratings / queryset.count()

    context = {
        'product': product,
        'avg_rating': round(avg_rating, 2),
        'rating_form': RatingForm()
    }

    return render(request, 'products/product_single.html', context)


def add_rating(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    user = request.user
    rating_form = RatingForm(data=request.POST)

    if rating_form.is_valid():
        rating = rating_form.save(commit=False)
        rating.product = product
        rating.user = user
        rating.save()
    else:
        rating_form = RatingForm()

    queryset = Rating.objects.filter(product=product_id)

    total_ratings = 0
    for result in queryset:
        total_ratings += result.rating

    avg_rating = total_ratings / queryset.count()

    context = {
        'product': product,
        'avg_rating': round(avg_rating, 2),
        'rating_form': RatingForm()
    }

    return render(request, 'products/product_single.html', context)