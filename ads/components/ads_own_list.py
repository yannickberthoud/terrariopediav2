from django_unicorn.components import UnicornView
from ads.models import Ads

class AdsOwnListView(UnicornView):
    owner = ""
    ads = Ads.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.owner = kwargs.get("owner")
        self.load(self.owner)

    def load(self, owner):
        self.ads = Ads.objects.filter(owner=int(owner)).order_by("-created_at")
        print(self.ads)