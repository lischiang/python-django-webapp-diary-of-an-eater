from django import forms
from dishes.models import Dish

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('name', 'place', 'date', 'description', 'price', 'rating')
