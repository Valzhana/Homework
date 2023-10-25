from django.urls import path
from .views import index
from .views import basket, sorted_basket

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('user/<int:user_id>/', basket, name='basket'),
    path('user_sorted/<int:user_id>/<int:days_ago>/', sorted_basket, name='sorted_basket'),

]
