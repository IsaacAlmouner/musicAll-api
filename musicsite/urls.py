#from django.contrib import admin
#from django.urls import include, path

#urlpatterns = [
 #  path('music/', include('music.urls')),
  #  path('admin/', admin.site.urls),]
  
from django.conf.urls import url, include
from django.contrib import admin
from graphene_django.views import GraphQLView
from .schema import schema
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql$', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]