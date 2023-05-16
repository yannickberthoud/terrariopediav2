from django_unicorn.components import UnicornView
from documentation.forms import DocumentationForm

class DocumentationFormView(UnicornView):
    form_class = DocumentationForm

    def get(self, request):
        context = {'form': self.form_class}
        return self.render_json_response(context)

    def post(self, request):
        form = DocumentationForm(request.POST)
        if form.is_valid():
            form.last_update_user = request.user
            form.save()
            form = DocumentationForm()
        context = {'form': form}
        return self.render_json_response(context)