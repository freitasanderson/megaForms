from rest_framework import serializers
from questionario.models import ItemQuestionario, ItemDependente, Respostas, QuemRespondeu

from questionario.serializers import OpcoesItemQuestionarioSerializer, RespostasSerializer
from questionario.serializers import ItemAssociativoSerializer

class ItemQuestionarioSerializer(serializers.ModelSerializer):
  
  alternativas = OpcoesItemQuestionarioSerializer(source='opcoesitemquestionario_set', many=True)
  respostas = RespostasSerializer(source='respostas_set', many=True)
  associacoes = ItemAssociativoSerializer(source='itemassociativo_set', many=True)

  class Meta:

    model = ItemQuestionario
    fields = ['id','tipo','descricao','ativo','respostas','alternativas','associacoes']