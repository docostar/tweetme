from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Tweet
# Create your views here.

def home_view(request,*args,**kwargs):
    return HttpResponse("<h2>Jai Bharat</h2>")

def tweet_detail_view(request,tweet_id):

    '''
        REST API VIEW
        Consume by Javascript or Swift or Java or Android/iOS
    '''
    try:
        obj=Tweet.objects.get(id=tweet_id)
    except:
        raise Http404

    return HttpResponse(f"<h2>Tweet no:{tweet_id}-{obj.content}</h2>")

    