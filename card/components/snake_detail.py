from django_unicorn.components import UnicornView
from django.shortcuts import get_object_or_404
from card.models import Snake


class SnakeDetailView(UnicornView):
    slug = None
    snake = Snake.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.slug = kwargs.get("slug")
        self.load()

    def load(self):
        self.snake = get_object_or_404(Snake, slug=self.slug)
