from django.shortcuts import render,redirect

from categories.models import Category


from .models import Expense
from .forms import ExpenseForm
from django.db.models import Model, Sum



# Create your views here.
def expense_list(request):
    expenses = Expense.objects.all()
    categories = Category.objects.all()
    
    category_id = request.GET.get('category')
    if category_id:
        expenses = expenses.filter(category_id=category_id)

        
        
    search = request.GET.get('search')
    if search:
        expenses = Expense.objects.filter(name__icontains=search)
        
    
    total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'total_expense': total_expense,'categories': categories})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect('expense_list')
    

