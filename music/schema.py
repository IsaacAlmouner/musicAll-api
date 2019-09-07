import graphene
from graphene_django.types import DjangoObjectType
from .models import Album, Artist, Song

class AlbumType(DjangoObjectType):
    class Meta:
        model = Album

class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist

class SongType(DjangoObjectType):
    class Meta:
        model = Song

class UpdateAlbumMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        album_name = graphene.String(required=True)
        id = graphene.ID()
    # The class attributes define the response of the mutation
    album = graphene.Field(AlbumType)
    def mutate(self, info, album_name, id):
        album = Album.objects.get(pk=id)
        album.album_name = album_name
        album.save()
        # Notice we return an instance of this mutation
        return UpdateAlbumMutation(album=album)

class ArtistInput(graphene.InputObjectType):
    id = graphene.ID()
    artist_name = graphene.String()
    
class CreateArtist(graphene.Mutation):
    class Arguments:
        input = ArtistInput(required=True)
    ok = graphene.Boolean()
    artist = graphene.Field(ArtistType)
    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        artist_instance = Artist(artist_name=input.artist_name)
        artist_instance.save()
        return CreateArtist(ok=ok, artist=artist_instance)

class UpdateArtistMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        artist_name = graphene.String(required=True)
        id = graphene.ID()
    # The class attributes define the response of the mutation
    artist = graphene.Field(ArtistType)
    def mutate(self, info, artist_name, id):
        artist = Artist.objects.get(pk=id)
        artist.artist_name = artist_name
        artist.save()
        # Notice we return an instance of this mutation
        return UpdateArtistMutation(artist=artist)

# class AlbumInput(graphene.InputObjectType):
#     id = graphene.ID()
#     album_name = graphene.String()
#     artists = graphene.List(ArtistInput)

# class CreateAlbum(graphene.Mutation):
#     class Arguments:
#         input = AlbumInput(required=True)
#     album = graphene.Field(AlbumType)
#     @staticmethod
#     def mutate(root, info, input=None):
#         artists = []
#         for artis_input in input.artists:
#           artist = Artist.objects.get(pk=artist_input.id)
#           if artist is None:
#             return CreateAlbum(ok=False, album=None)
#           artists.append(artist)
#         album_instance = album(album_name=input.album_name,)
#         album_instance.save()
#         album_instance.artists.set(artists)
#         return CreateAlbum(album=album_instance)

class Mutation(graphene.ObjectType):
    update_album = UpdateAlbumMutation.Field()
    update_artist = UpdateArtistMutation.Field()
    crete_artist = CreateArtist.Field()
    #create_album = CreateAlbum.Field()

class Query(object):
    album = graphene.Field(AlbumType, id=graphene.Int(), album_name=graphene.String())
    all_albums = graphene.List(AlbumType)
    artist = graphene.Field(ArtistType, id=graphene.Int(), artist_name=graphene.String())
    all_artists = graphene.List(ArtistType)
    song = graphene.Field(SongType, id=graphene.Int(), song_name=graphene.String())
    all_songs = graphene.List(SongType)
    
    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()
    
    def resolve_all_albums(self, info, **kwargs):
         return Album.objects.all()
    
    def resolve_all_songs(self, info, **kwargs):
        #return Song.objects.select_related('allbum').all()
        return Song.objects.all()
    
    def resolve_album(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('album_name')
        if id is not None:
            return Album.objects.get(pk=id)
        if name is not None:
            return Album.objects.get(album_name=name)
        return None

    def resolve_artist(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('artist_name')
        if id is not None:
            return Artist.objects.get(pk=id)
        if name is not None:
            return Artist.objects.get(artist_name=name)
        return None
    
    def resolve_song(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('song_name')
        if id is not None:
            return Song.objects.get(pk=id)
        if name is not None:
            return Song.objects.get(song_name=name)
        return None

        
        
    


    
    
    