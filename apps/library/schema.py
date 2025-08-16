import graphene
from apps.library.gql import gql_queries
from graphene_django.filter import DjangoFilterConnectionField


class Query(graphene.ObjectType):
    libraries = DjangoFilterConnectionField(gql_queries.LibraryGQLType)


schema = graphene.Schema(query=Query)
