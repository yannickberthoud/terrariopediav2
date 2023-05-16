from django_unicorn.components import UnicornView
from django.contrib.auth.models import User

class MemberListView(UnicornView):
    query = ""
    members = User.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.query = kwargs.get("query")
        self.load(self.query)

    def load(self, query):
        if query == "all":
            self.members = User.objects.order_by("last_name", "first_name")