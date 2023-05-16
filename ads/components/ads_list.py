from django_unicorn.components import UnicornView
from ads.models import Ads

class AdsListView(UnicornView):
    category = ""
    ads = Ads.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.category = kwargs.get("category")
        self.load(self.category)

    def load(self, category):
        if category:
            self.ads = Ads.objects.filter(category__iexact=category).order_by("-created_at")
        else:
            self.ads = Ads.objects.order_by('genus', 'species')
