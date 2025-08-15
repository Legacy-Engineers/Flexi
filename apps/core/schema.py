import graphene
from apps.core.app_loader import AppLoader


queries = AppLoader.get_app_graphql_schema()[0]
mutations = AppLoader.get_app_graphql_schema()[1]


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(graphene.ObjectType):
    pass


# Create a combined schema by merging all queries and mutations
def create_combined_schema():
    # Create a dictionary to hold all fields
    query_fields = {}
    mutation_fields = {}

    # Collect fields from other app queries
    for query_class in queries:
        if (
            query_class
            and hasattr(query_class, "_meta")
            and hasattr(query_class._meta, "fields")
        ):
            for field_name, field in query_class._meta.fields.items():
                if field_name not in query_fields:
                    query_fields[field_name] = field

    # Collect fields from other app mutations
    for mutation_class in mutations:
        if (
            mutation_class
            and hasattr(mutation_class, "_meta")
            and hasattr(mutation_class._meta, "fields")
        ):
            for field_name, field in mutation_class._meta.fields.items():
                if field_name not in mutation_fields:
                    mutation_fields[field_name] = field

    # Create combined classes with all fields
    combined_query = type("CombinedQuery", (Query,), query_fields)
    combined_mutation = type("CombinedMutation", (Mutation,), mutation_fields)

    return graphene.Schema(query=combined_query, mutation=combined_mutation)


schema = create_combined_schema()
