from django_unicorn.components import UnicornView
from django.shortcuts import get_object_or_404
from member.models import Profile
from django.contrib.auth.models import User

class MemberDetailView(UnicornView):
    profile = Profile.objects.none()
    user = User.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        pk = kwargs.get("pk")
        self.load(pk)

    def load(self, pk):
        self.profile = get_object_or_404(Profile, pk=pk)
        self.user = get_object_or_404(User, pk=pk)
