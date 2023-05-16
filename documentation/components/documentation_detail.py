from django_unicorn.components import UnicornView
from django.shortcuts import get_object_or_404
from documentation.models import Documentation

class DocumentationDetailView(UnicornView):
    slug = None
    documentation = Documentation.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.slug = kwargs.get("slug")
        self.load()

    def load(self):
        self.documentation = get_object_or_404(Documentation, slug=self.slug)



