from django_unicorn.components import UnicornView
from django.shortcuts import get_object_or_404
from card.models import Lizard

class LizardDetailView(UnicornView):
    slug = None
    lizard = Lizard.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.slug = kwargs.get("slug")
        self.load()

    def load(self):
        self.lizard = get_object_or_404(Lizard, slug=self.slug)
