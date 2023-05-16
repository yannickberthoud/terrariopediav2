from django_unicorn.components import UnicornView
from card.forms import ArthropodForm

class ArthropodFormView(UnicornView):
    form_class = ArthropodForm

    def get(self, request):
        context = {'form': self.form_class}
        return self.render_json_response(context)

    def post(self, request):
        form = ArthropodForm(request.POST)
        if form.is_valid():
            form.save()
            form = ArthropodForm()
        context = {'form': form}
        return self.render_json_response(context)