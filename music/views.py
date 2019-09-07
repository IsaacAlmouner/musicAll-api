from django.http import HttpResponse
from .models import Album, Artist, Song
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_album_list = Album.objects.order_by('id')[:5]
    context = {'latest_album_list': latest_album_list,}
    return render(request, 'music/index.html', context)

def albumDetail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/albumDetail.html', {'question': album})
    
