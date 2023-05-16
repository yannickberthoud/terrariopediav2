from django_unicorn.components import UnicornView
from documentation.models import Documentation


class DocumentationListView(UnicornView):
    category = ""
    documentations = Documentation.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.category = kwargs.get("category")
        self.load(self.category)

    def load(self, category):
        self.documentations = Documentation.objects.filter(category__iexact=category).order_by("-created_at")