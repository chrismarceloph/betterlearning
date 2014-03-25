from allauth.account.forms import LoginForm
from vanilla import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        kwargs['form'] = LoginForm()
        return kwargs
