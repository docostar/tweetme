from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from .models import Tweet
# Create your views here.



def home_view(request,*args,**kwargs):
    #return HttpResponse("<h2>Jai Bharat</h2>")
    return render(request,"pages/home.html",status=200,context={})

def tweet_list_view(request,*args, **kwargs):
    qs=Tweet.objects.all()
    tweets_list=[{"id":x.id,"content":x.content} for x in qs]
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
    