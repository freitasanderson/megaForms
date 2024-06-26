from django.contrib import admin
from django import forms
from django.contrib.admin.options import StackedInline
from questionario.models import ItemQuestionario, OpcoesItemQuestionario, ItemAssociativo
from django_summernote.admin import SummernoteModelAdmin

class OpcoesItemQuestionarioInline(StackedInline):
    extra = 0
    model = OpcoesItemQuestionario

class ItemAssociativoInline(StackedInline):
    extra = 0
    model = ItemAssociativo

@admin.register(ItemQuestionario)
class ItemQuestionarioAdmin(SummernoteModelAdmin):
    list_display = ('id','questionario','tipo','descricao','ativo')
    search_fields = ['id','questionario','descricao']
    autocomplete_fields = ['questionario']
    summernote_fields = ('descricao')
    icon_name = 'dehaze'
    inlines = [
        OpcoesItemQuestionarioInline,
        ItemAssociativoInline
    ]
    actions = ['criarOpcoesQuestionarioEscolar']
    # class Media:
    #     js = ('assets/JS/admin/ScriptQuestionarioAdmin.js',)    
    #     css = {
    #          'all': ('assets/CSS/admin/QuestionarioAdmin.css',)
    #     }

    
    def criarOpcoesQuestionarioEscolar(modeladmin, request, queryset):
        for pergunta in queryset.filter(questionario__tipoDoQuestionario=0):
            opcoes = OpcoesItemQuestionario.objects.filter(pergunta=pergunta)

            if opcoes.exists():
                jaTemAlguma = True
            else:
                jaTemAlguma = False
            
            if not jaTemAlguma:
                opcaoSim = OpcoesItemQuestionario()
                opcaoSim.pergunta = pergunta
                opcaoSim.valor = 'Sim'
                opcaoSim.save()

                opcaoNao = OpcoesItemQuestionario()
                opcaoNao.pergunta = pergunta
                opcaoNao.valor = 'Não'
                opcaoNao.save()

                opcaoNSA = OpcoesItemQuestionario()
                opcaoNSA.pergunta = pergunta
                opcaoNSA.valor = 'Não se aplica'
                opcaoNSA.save()
            else:

                temSim = opcoes.filter(valor='Sim').exists()
                if not temSim:
                    opcaoSim = OpcoesItemQuestionario()
                    opcaoSim.pergunta = pergunta
                    opcaoSim.valor = 'Sim'
                    opcaoSim.save()

                temNao = opcoes.filter(valor='Não').exists()
                if not temNao:
                    opcaoNao = OpcoesItemQuestionario()
                    opcaoNao.pergunta = pergunta
                    opcaoNao.valor = 'Não'
                    opcaoNao.save()

                temNSA = opcoes.filter(valor='Não se aplica').exists()
                if not temNSA:
                    opcaoNSA = OpcoesItemQuestionario()
                    opcaoNSA.pergunta = pergunta
                    opcaoNSA.valor = 'Não se aplica'
                    opcaoNSA.save()

    criarOpcoesQuestionarioEscolar.short_description = "Criar Opões de resposta para os questionários escolares"