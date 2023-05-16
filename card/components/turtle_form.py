from django_unicorn.components import UnicornView
from card.forms import TurtleForm

class TurtleFormView(UnicornView):
    form_class = TurtleForm

    def get(self, request):
        context = {'form': self.form_class}
        return self.render_json_response(context)

    def post(self, request):
        form = TurtleForm(request.POST)
        if form.is_valid():
            form.save()
            form = TurtleForm()
        context = {'form': form}
        return self.render_json_response(context)