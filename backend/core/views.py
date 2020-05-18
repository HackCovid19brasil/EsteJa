from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Diagnostico
from .forms import DiagnosticoForm
from .tree import tree

def index(request):
    return render(request, 'index.html', {})

def info(request):
    return render(request, 'core/info.html', {})

def info_statistic(request):
    return render(request, 'core/info_statistic.html', {})


class DiagnosticoViewMixin(UserPassesTestMixin):
    model = Diagnostico

    def test_func(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super(DiagnosticoViewMixin, self).get_context_data(**kwargs)
        context["model_type"] = self.model.__name__
        return context


class DiagnosticoView(DiagnosticoViewMixin, UpdateView):
    form_class = DiagnosticoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Diagnosticar"
        return context

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        return self.render_to_response(
            self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = None
        diagnostico = tree(self, request.POST)
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, diagnostico, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, diagnostico, **kwargs):
        # import ipdb; ipdb.set_trace()
        self.object = form.save()
        context = self.get_context_data(**kwargs)
        context["mensagem"] = diagnostico
        context["form"] = form
        return self.render_to_response(context)
