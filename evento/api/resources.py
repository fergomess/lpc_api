from tastypie.resources import ModelResource
from tastypie import fields, utils
from tastypie.authorization import Authorization
from evento.models import *
from django.contrib.auth.models import User


class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all() #lista ou consulta do recurso
        allowed_methods = ['get','post','put','delete']
        filtering = { #aplicações de filtros, recebe um json
            "descricao": ('exact', 'startswith',) #o campo descrição é para fornecer dois tipos de filtros, passando a palavra exata e um tipo de filtro
        }
        authorization = Authorization() #permite que qualquer pessoa faça requisições (chamadas) para APIS (chamadas Put)

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']
        authorization = Authorization() #permite que qualquer pessoa faça requisições (chamadas) para APIS (chamadas Put)

class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
        authorization = Authorization()

class EventoResource(ModelResource):
    realizador  = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get','post','put','delete'] #tipos de métodos
        authorization = Authorization()

class EventoCientificoResource(ModelResource):
    realizador  = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
        authorization = Authorization()

class PessoaFisicaResource(ModelResource):
    class Meta:
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
        authorization = Authorization()

class PessoaJuridicaResource(ModelResource):
    class Meta:
        queryset = PessoaJuridica.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()

class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()

class ArtigoCientificoResource(ModelResource):
    evento = fields.ToOneField(EventoCientificoResource, 'evento')
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "titulo": ('exact', 'startswith',)
        }
        authorization = Authorization()

class InscricoesResource(ModelResource):
    pessoa = fields.ToOneField(PessoaFisicaResource, 'pessoa') #diz que é pra fazer o relacionamento de chave estrangeira, e na tela mostra a referencia da pessoa: URL
    evento = fields.ToOneField(EventoResource, 'evento')
    tipoInscricao = fields.ToOneField(TipoInscricaoResource, 'tipoInscricao')
    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()
        filtering = {
            "tipoInscricao": ('exact', 'startswith',)
        }

class ArtigoAutorResource(ModelResource):
    artigoCientifico = fields.ToOneField(ArtigoCientificoResource, 'artigoCientifico')
    autor = fields.ToOneField(AutorResource, 'autor')
    class Meta:
        queryset = ArtigoAutor.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()
