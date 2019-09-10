from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    artist_image= models.CharField(max_length=500)
    def __str__(self):
        return self.artist_name    
    def __strimg__(self):
        return self.artist_image

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=200)
    album_image= models.CharField(max_length=500)
    def __str__(self):
        return self.album_name
    def __strimg__(self):
        return self.album_image

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=200)
    song_image= models.CharField(max_length=500)
    def __str__(self):
        return self.song_name
    def __strimg__(self):
        return self.song_image