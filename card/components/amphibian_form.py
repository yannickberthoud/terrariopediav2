from django_unicorn.components import UnicornView
from card.forms import AmphibianForm

class AmphibianFormView(UnicornView):
    form_class = AmphibianForm

    def get(self, request):
        context = {'form': self.form_class}
        return self.render_json_response(context)

    def post(self, request):
        form = AmphibianForm(request.POST)
        if form.is_valid():
            form.save()
            form = AmphibianForm()
        context = {'form': form}
        return self.render_json_response(context)