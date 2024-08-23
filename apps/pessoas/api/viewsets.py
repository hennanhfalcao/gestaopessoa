import requests

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.pessoas.models import Pessoa, Endereco
from apps.pessoas.api.serializers import PessoaSerializer, EnderecoSerializer

class PessoaViewSet(ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def create(self, request, *args, **kwargs):
        cep = request.data.get("cep")
        
        
        requisicao = requests.get(f"viacep.com.br/ws/{cep}/json/")


        endereco_salvo = Endereco.objects.create(
            cep=requisicao["cep"],
            bairro=requisicao["bairro"],
            logradouro=requisicao["logradouro"]
        )

        return Response({"Sucesso: endereco salco"},
                        status = status.HTTP_201_CREATED)
