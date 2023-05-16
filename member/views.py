from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UpdateUserForm, ProfileForm
from django.views.generic import DetailView, ListView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from .models import Profile

from django.contrib.auth.models import User

def CommunityList(request):
    return render(request, "member/member-list.html")

def CommunityDetail(request, pk):
    return render(request, "member/member-detail.html", {"pk": pk})

class CommunityDetailView(DetailView):
    model = User
    template_name = 'member/community_details.html'
    context_object_name = 'object'

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'member/change_password.html'
    success_message = "Votre mot de passe a été mis à jour."
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class MemberUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'member/member-form.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('member:member-detail', kwargs={'pk': self.object.user.pk})

@method_decorator(login_required, name='dispatch')
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Votre profil a été mis à jour.')
            return redirect(to='profile')
    else:
        try:
            profile = request.user.profile
        except ObjectDoesNotExist:
            profile = Profile()
            profile.user = request.user
            profile.save()
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'member/profile.html', {'current_user': request.user.pk, 'user_form': user_form, 'profile_form': profile_form})