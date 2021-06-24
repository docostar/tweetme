from tweetme.settings import ALLOWED_HOSTS
from django import forms
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings
from .models import Tweet
from .forms import TweetForm
import random
# Create your views here.

ALLOWED_HOSTS=settings.ALLOWED_HOSTS

def home_view(request,*args,**kwargs):
    #return HttpResponse("<h2>Jai Bharat</h2>")
    return render(request,"pages/home.html",status=200,context={})

def tweet_create_view(request,*args, **kwargs):
    form = TweetForm(request.POST or None)
    # print("post data is:",request.POST)
    next_url=request.POST.get("next") or None
    # print("Next Url",next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(),status=201) #201- for creating 
        if next_url!=None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/forms.html', context={"form": form})

def tweet_list_view(request,*args, **kwargs):
    qs=Tweet.objects.all()
    #tweets_list=[{"id":x.id,"content":x.content,"likes":random.randint(0,50)} for x in qs]
    tweets_list=[x.serialize() for x in qs]
    data={
        "isUser":False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request,tweet_id):

    '''
        REST API VIEW
        Consume by Javascript or Swift or Java or Android/iOS
    '''
    data={
            "id": tweet_id
           # "content": obj.content,
            #"image": obj.image.url

        }
    status=200    
    try:
        obj=Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        #raise Http404
        data['Message']="Not Found"
        status=404

    #return HttpResponse(f"<h2>Tweet no:{tweet_id}-{obj.content}</h2>")
    return JsonResponse(data,status=status)
    