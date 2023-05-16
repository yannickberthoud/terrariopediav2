from django_unicorn.components import UnicornView
from card.models import Turtle


class TurtleListView(UnicornView):
    show_quantity = 0
    turtles = Turtle.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.show_quantity = kwargs.get("quantity")
        self.load(self.show_quantity)

    def load(self, quantity):
        if self.show_quantity != 0:
            self.turtles = Turtle.objects.order_by('genus', 'species')[:quantity]
        else:
            self.turtles = Turtle.objects.order_by('genus', 'species')