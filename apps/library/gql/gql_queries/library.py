import graphene
from graphene_django import DjangoObjectType
from apps.library.models import Library


class LibraryGQLType(DjangoObjectType):
    class Meta:
        model = Library
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "name": ["exact", "icontains"],
            "base_dir": ["exact", "icontains"],
            "description": ["exact", "icontains"],
        }
