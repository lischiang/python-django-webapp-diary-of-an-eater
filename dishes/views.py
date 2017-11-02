from django.shortcuts import render, redirect
from dishes.models import Dish
from dishes.forms import DishForm
from django.views.generic import DetailView

'''def add(request):
    p = Dish(name='New Dish', place='Some restaurant', date='2016-04-23 14:30:59', description='It was good',
    price=25.00, rating=7)
    p.save()
    return render(request, 'dishes/add.html')'''

# view to make a new dish
def dish_new(request):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save(commit=False)
            #commit=False is not to commit yet the new dish, but wait to add other fields (like author)
            '''dish.author = request.user'''
            dish.save()
            # redirect to this dish_details url
            return redirect('dish_details', pk=dish.pk)
        
    else:
        form = DishForm()
    return render(request, 'dishes/dish_edit.html', {'form': form})

# not used
class DishDetail(DetailView):
    model = Dish
    template_name = "dishes/dish.html"
