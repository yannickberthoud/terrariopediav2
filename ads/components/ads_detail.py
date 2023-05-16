from django_unicorn.components import UnicornView
from django.shortcuts import get_object_or_404
from ads.models import Ads

class AdsDetailView(UnicornView):
    pk = 0
    ads = Ads.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.slug = kwargs.get("slug")
        self.load()

    def load(self):
        self.ads = get_object_or_404(Ads, pk=self.pk)