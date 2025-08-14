from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from apps.core.app_loader import AppLoader

app_urls = AppLoader.get_app_urls()

urlpatterns = [
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

# Include app URLs
for app_url in app_urls:
    if app_url:
        urlpatterns.append(path("", include(app_url)))
