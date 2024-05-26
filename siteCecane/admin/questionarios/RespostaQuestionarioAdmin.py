from django.contrib import admin
from django import forms

from siteCecane.models import RespostasQuestionario, Respostas


@admin.register(RespostasQuestionario)
class RespostasQuestionarioAdmin(admin.ModelAdmin):
    list_display = ('id','escola','questionario','pergunta','valor')
    
    autocomplete_fields = ['quemCadastrou',]
    readonly_fields = ['quemCadastrou',]
    icon_name='drag_handle'
    actions = ['criarRespostasQuestionarioEscolar']
    list_filter = ['questionario__tipoDoQuestionario',]
    list_per_page = 10000

    def save_model(self, request, obj, form, change):

        if not obj.quemCadastrou:
            obj.quemCadastrou = request.user
		
        super(RespostasQuestionarioAdmin, self).save_model(request, obj, form, change)

    def criarRespostasQuestionarioEscolar(modeladmin, request, queryset):
        print(f'Total de Respostas: {queryset.count()}-{queryset.filter(questionario__tipoDoQuestionario=0).count()}')
        for resposta in queryset.filter(questionario__tipoDoQuestionario=0):
            respondido = Respostas.objects.filter(questionario=resposta.questionario,
                                                  escola=resposta.escola,
                                                  pergunta=resposta.pergunta,
                                                  quemCadastrou=resposta.quemCadastrou
                                                )
            
            # print(f'Resposta: {resposta.get_valor_display()}')
            if respondido.exists():
                print(f'Já respondido')
            else:

                novaResposta = Respostas(questionario=resposta.questionario,
                                        escola=resposta.escola,
                                        pergunta=resposta.pergunta,
                                        quemCadastrou=resposta.quemCadastrou,
                                        valor=resposta.get_valor_display()
                                    )
                novaResposta.save()
                
                      

    criarRespostasQuestionarioEscolar.short_description = "Migrar respostas dos questionários escolares"