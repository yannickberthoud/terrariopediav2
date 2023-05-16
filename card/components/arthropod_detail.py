from django_unicorn.components import UnicornView
from django.shortcuts import get_object_or_404
from card.models import Arthropod

class ArthropodDetailView(UnicornView):
    slug = None
    arthropod = Arthropod.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.slug = kwargs.get("slug")
        self.load()

    def load(self):
        self.arthropod = get_object_or_404(Arthropod, slug=self.slug)
