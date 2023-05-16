from django_unicorn.components import UnicornView
from django.shortcuts import get_object_or_404
from card.models import Turtle

class TurtleDetailView(UnicornView):
    slug = None
    turtle = Turtle.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.slug = kwargs.get("slug")
        self.load()

    def load(self):
        self.turtle = get_object_or_404(Turtle, slug=self.slug)
