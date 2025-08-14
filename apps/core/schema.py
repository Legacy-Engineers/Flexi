import graphene
from apps.core.app_loader import AppLoader


queries = AppLoader.get_app_graphql_schema()[0]
mutations = AppLoader.get_app_graphql_schema()[1]


class Mutation(graphene.ObjectType, *mutations):
    pass


class Query(graphene.ObjectType, *queries):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query, mutation=Mutation)
