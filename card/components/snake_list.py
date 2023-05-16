from django_unicorn.components import UnicornView
from card.models import Snake


class SnakeListView(UnicornView):
    show_quantity = int
    snakes = Snake.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.show_quantity = kwargs.get("quantity")
        self.load(self.show_quantity)

    def load(self, quantity):
        if self.show_quantity != 0:
            self.snakes = Snake.objects.order_by('genus', 'species')[:quantity]
        else:
            self.snakes = Snake.objects.order_by('genus', 'species')