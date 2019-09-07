from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:album_id>/', views.albumDetail, name='detail'),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]