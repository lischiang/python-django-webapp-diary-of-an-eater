from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from dishes.models import Dish
from . import views

urlpatterns = [ url(r'^$', ListView.as_view(queryset=Dish.objects.all().order_by("-date")[:25],
                                            template_name="dishes/dishes.html"), name="dishes"),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Dish,
                                                        template_name = 'dishes/dish.html'), name="dish_details"),
                url(r'^new/',views.dish_new, name='dish_new'),
                ]
#from dishes.views import DishDetail
#url(r'^(?P<pk>\d+)$', DishDetail.as_view(), name='dish_detail'),


