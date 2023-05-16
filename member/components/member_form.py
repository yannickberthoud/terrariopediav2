from django_unicorn.components import UnicornView
from member.forms import ProfileForm

class MemberFormView(UnicornView):
    form_class = ProfileForm

    def get(self, request):
        context = {'form': self.form_class}
        return self.render_json_response(context)

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProfileForm()
        context = {'form': form}
        return self.render_json_response(context)