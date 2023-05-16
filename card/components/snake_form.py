from django_unicorn.components import UnicornView
from card.forms import SnakeForm

class SnakeFormView(UnicornView):
    form_class = SnakeForm

    def get(self, request):
        context = {'form': self.form_class}
        return self.render_json_response(context)

    def post(self, request):
        form = SnakeForm(request.POST)
        if form.is_valid():
            form.save()
            form = SnakeForm()
        context = {'form': form}
        return self.render_json_response(context)