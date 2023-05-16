from django_unicorn.components import UnicornView
from card.models import Amphibian


class AmphibianListView(UnicornView):
    show_quantity = 0
    amphibians = Amphibian.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.show_quantity = kwargs.get("quantity")
        self.load(self.show_quantity)

    def load(self, quantity):
        if self.show_quantity != 0:
            self.amphibians = Amphibian.objects.order_by('genus', 'species')[:quantity]
        else:
            self.amphibians = Amphibian.objects.order_by('genus', 'species')
