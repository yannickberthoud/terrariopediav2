from django_unicorn.components import UnicornView
from django.shortcuts import get_object_or_404
from card.models import Amphibian

class AmphibianDetailView(UnicornView):
    slug = None
    amphibian = Amphibian.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.slug = kwargs.get("slug")
        self.load()

    def load(self):
        self.amphibian = get_object_or_404(Amphibian, slug=self.slug)



