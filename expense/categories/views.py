from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm


# Create your views here.
def category_list(request):
    categories = Category.objects.all()
    return render(request, "categories/category_list.html", {"categories": categories})


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_expense")
    else:
        form = CategoryForm()
    return render(request, "categories/add_category.html", {"form": form})

def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect("category_list")