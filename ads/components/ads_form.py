from django_unicorn.components import UnicornView
from ads.forms import AdsForm

class AdsFormView(UnicornView):
    form_class = AdsForm

    def get(self, request):
        context = {'form': self.form_class}
        return self.render_json_response(context)

    def post(self, request):
        form = AdsForm(request.POST)
        if form.is_valid():
            form.save()
            form = AdsForm()
        context = {'form': form}
        return self.render_json_response(context)