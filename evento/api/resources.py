from tastypie.resources import ModelResource
from evento.models import TipoInscricao, Pessoa
from django.contrib.auth.models import User

#Tastypie
#Mapiar o que vai ser disponibilizado na API
#MetaInformações

class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get']


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        resource_name = 'p' #altera o nome para p -> http://localhost:8000/api/v1/p/?format=json
        allowed_methods = ['get']
