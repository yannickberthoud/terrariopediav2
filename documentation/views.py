from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from .models import Documentation
from .forms import DocumentationForm

def DocumentationList(request, category):
    return render(request, "documentation/documentation-list.html", {"category": category})

def DocumentationDetail(request, category, slug):
    return render(request, "documentation/documentation-detail.html", {"category": category,"slug": slug})

@method_decorator(login_required, name='dispatch')
class DocumentationCreateView(CreateView):
    model = Documentation
    form_class = DocumentationForm
    template_name = 'documentation/documentation-form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.last_update_user = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        category = ""
        if self.object.category == 'A':
            category = "amphibiens"
        elif self.object.category == 'R':
            category = "arthropodes"
        elif self.object.category == 'L':
            category = "lezards"
        elif self.object.category == 'S':
            category = "serpents"
        elif self.object.category == 'T':
            category = "tortues"
        return reverse('documentation:documentation-detail', kwargs={'category': category, 'slug': self.object.slug})

@method_decorator(login_required, name='dispatch')
class DocumentationUpdateView(UpdateView):
    model = Documentation
    form_class = DocumentationForm
    template_name = 'documentation/documentation-form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.last_update_user = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        category = ""
        if self.object.category == 'A':
            category = "amphibiens"
        elif self.object.category == 'R':
            category = "arthropodes"
        elif self.object.category == 'L':
            category = "lezards"
        elif self.object.category == 'S':
            category = "serpents"
        elif self.object.category == 'T':
            category = "tortues"
        return reverse('documentation:documentation-detail', kwargs={'category': category, 'slug': self.object.slug})
