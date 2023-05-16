from django.shortcuts import render
from .models import Amphibian, Arthropod, Lizard, Snake, Turtle
from .forms import AmphibianForm, ArthropodForm, LizardForm, SnakeForm, TurtleForm
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse

def AmphibianList(request):
    return render(request, "card/amphibian-list.html")

def AmphibianDetail(request, slug):
    return render(request, "card/amphibian-detail.html", {"slug": slug})

def ArthropodList(request):
    return render(request, "card/arthropod-list.html")

def ArthropodDetail(request, slug):
    return render(request, "card/arthropod-detail.html", {"slug": slug})

def LizardList(request):
    return render(request, "card/lizard-list.html")

def LizardDetail(request, slug):
    return render(request, "card/lizard-detail.html", {"slug": slug})

def SnakeList(request):
    return render(request, "card/snake-list.html")

def SnakeDetail(request, slug):
    return render(request, "card/snake-detail.html", {"slug": slug})

def TurtleList(request):
    return render(request, "card/turtle-list.html")

def TurtleDetail(request, slug):
    return render(request, "card/turtle-detail.html", {"slug": slug})

# Formulaires
@method_decorator(login_required, name='dispatch')
class SnakeCreateView(CreateView):
    model = Snake
    form_class = SnakeForm
    template_name = 'card/snake-form.html'

    def form_valid(self, form):
        form.instance.last_owner = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('card:snake-detail', kwargs={'slug': self.object.slug})

@method_decorator(login_required, name='dispatch')
class SnakeUpdateView(UpdateView):
    model = Snake
    form_class = SnakeForm
    template_name = 'card/snake-form.html'

    def form_valid(self, form):
        form.instance.last_owner = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('card:snake-detail', kwargs={'slug': self.object.slug})

@method_decorator(login_required, name='dispatch')
class AmphibianCreateView(CreateView):
    model = Amphibian
    form_class = AmphibianForm
    template_name = 'card/amphibian-form.html'

    def form_valid(self, form):
        form.instance.last_owner = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('card:amphibian-detail', kwargs={'slug': self.object.slug})

@method_decorator(login_required, name='dispatch')
class AmphibianUpdateView(UpdateView):
    model = Amphibian
    form_class = AmphibianForm
    template_name = 'card/amphibian-form.html'

    def form_valid(self, form):
        form.instance.last_owner = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('card:amphibian-detail', kwargs={'slug': self.object.slug})

@method_decorator(login_required, name='dispatch')
class LizardCreateView(CreateView):
    model = Lizard
    form_class = LizardForm
    template_name = 'card/lizard-form.html'

    def form_valid(self, form):
        form.instance.last_owner = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('card:lizard-detail', kwargs={'slug': self.object.slug})

@method_decorator(login_required, name='dispatch')
class LizardUpdateView(UpdateView):
    model = Lizard
    form_class = LizardForm
    template_name = 'card/lizard-form.html'

    def form_valid(self, form):
        form.instance.last_owner = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('card:lizard-detail', kwargs={'slug': self.object.slug})

@method_decorator(login_required, name='dispatch')
class ArthropodCreateView(CreateView):
    model = Arthropod
    form_class = ArthropodForm
    template_name = 'card/arthropod-form.html'

    def form_valid(self, form):
        form.instance.last_owner = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('card:arthropod-detail', kwargs={'slug': self.object.slug})

@method_decorator(login_required, name='dispatch')
class ArthropodUpdateView(UpdateView):
    model = Arthropod
    form_class = ArthropodForm
    template_name = 'card/arthropod-form.html'

    def form_valid(self, form):
        form.instance.last_owner = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('card:arthropod-detail', kwargs={'slug': self.object.slug})

@method_decorator(login_required, name='dispatch')
class TurtleCreateView(CreateView):
    model = Turtle
    form_class = TurtleForm
    template_name = 'card/turtle-form.html'

    def form_valid(self, form):
        form.instance.last_owner = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('card:turtle-detail', kwargs={'slug': self.object.slug})

@method_decorator(login_required, name='dispatch')
class TurtleUpdateView(UpdateView):
    model = Turtle
    form_class = TurtleForm
    template_name = 'card/turtle-form.html'

    def form_valid(self, form):
        form.instance.last_owner = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('card:turtle-detail', kwargs={'slug': self.object.slug})