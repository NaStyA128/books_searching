from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SearchForm

# Create your views here.


class HomeView(FormView):
    form_class = SearchForm
    template_name = 'index.html'

    def form_valid(self, form):
        # result_form = form.start()
        # if result_form:
        return HttpResponseRedirect('/result/')
        # else:
        #     return HttpResponse('Ошибка поиска.')


class ResultView(TemplateView):
    template_name = 'info_user.html'
