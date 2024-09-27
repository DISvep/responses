from django.shortcuts import render, redirect
from .models import Product, Review
from .forms import ReviewForm


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(
        request,
        'product_list.html',
        context=context
    )


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    reviews = product.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()

            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'form': form
    }

    return render(
        request,
        'product_detail.html',
        context=context
    )
