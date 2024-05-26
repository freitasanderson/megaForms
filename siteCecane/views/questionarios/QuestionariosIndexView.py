from typing import Any
from django import http
from django.http import HttpResponse
from django.http.response import HttpResponse

from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from siteCecane.models import TipoQuestionario, ItemQuestionario, RespostasQuestionario,RespostasAlternativoQuestionario

from siteCecane.views import BasePermissoesView

class QuestionariosIndexView(LoginRequiredMixin,BasePermissoesView,TemplateView):

    template_name = "siteCecane/questionarios/indexQuestionarios.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['questionario'] = TipoQuestionario.objects.filter(ativo=True).order_by('nome')

        # context['perguntas'] = ItemQuestionario.objects.all().filter(ativo=True)

        if self.ehSuperUser or self.ehGestor:

            context['respondidos'] = RespostasQuestionario.objects.all().order_by('questionario__id','escola')
            context['respondidos2'] = RespostasAlternativoQuestionario.objects.all().order_by('questionario__id')

                
        else:

            context['respondidos'] = RespostasQuestionario.objects.filter(quemCadastrou=self.request.user).order_by('questionario__id','escola')
            context['respondidos2'] = RespostasAlternativoQuestionario.objects.all().order_by('questionario__id')

        context['questionariosRespondidos'] = []

        for resposta in context['respondidos2']:

            context['questionariosRespondidos'].append(resposta.questionario)

        context['questionariosRespondidos'] = list(set(context['questionariosRespondidos']))


        return context
