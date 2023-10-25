import random

from django.core.management.base import BaseCommand
from ...models import User
from ...models import Product
from ...models import Order


class Command(BaseCommand):
    help = "generate fake data"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="User ID")

    def handle(self, *args, **kwargs):
        user_list = []
        product_list = []
        count = kwargs.get('count')

        for j in range(10):
            product = Product(name=f'PName{j}', price=f'{j + 1}0', description=f'text-{j}', quantity=f'{j}')
            product.save()
            product_list.append(product)

        for i in range(1, count + 1):
            user = User(name=f'Name{i}', email=f'mail{i}.mail.ru', password=f'pass{i}', phone=f'123-{i}',
                        address=f'address{i}')
            user.save()
            user_list.append(user)

        for k in range(1, 6):

            user_rnd = random.randint(0, count - 1)

            order = Order(customer=user_list[user_rnd])
            total_price = 0
            for l in range(0, 10):
                if random.randint(0, 1) == 1:
                    total_price += float(product_list[l].price)
                    order.total_price = total_price
                    order.save()
                    order.products.add(product_list[l])
