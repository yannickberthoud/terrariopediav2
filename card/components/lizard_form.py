from django_unicorn.components import UnicornView
from card.forms import LizardForm

class LizardFormView(UnicornView):
    form_class = LizardForm

    def get(self, request):
        context = {'form': self.form_class}
        return self.render_json_response(context)

    def post(self, request):
        form = LizardForm(request.POST)
        if form.is_valid():
            form.save()
            form = LizardForm()
        context = {'form': form}
        return self.render_json_response(context)