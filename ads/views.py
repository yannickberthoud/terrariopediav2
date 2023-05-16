from django.shortcuts import render
from .models import Ads
from .forms import AdsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy

def AdsList(request):
    return render(request, "ads/ads-list.html")

def AdsOwnList(request):
    return render(request, "ads/ads-own-list.html", {'owner': request.user.pk})

def AdsDetail(request, pk):
    return render(request, "ads/ads-detail.html", {"pk": pk})

@method_decorator(login_required, name='dispatch')
class AdsCreateView(CreateView):
    model = Ads
    form_class = AdsForm
    template_name = 'ads/ads-form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ads:ads-detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class AdsUpdateView(UpdateView):
    model = Ads
    form_class = AdsForm
    template_name = 'ads/ads-form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ads:ads-detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class AdsDeleteView(DeleteView):
    model = Ads
    success_url = reverse_lazy("ads:ads-list")