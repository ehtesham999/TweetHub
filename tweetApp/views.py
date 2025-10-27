from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Tweet
from .forms import TweetForm
# Create your views here.
def home(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweet_list.html',{'tweets':tweets})

def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('list')
    else:
        form = TweetForm()
        return render(request, 'tweet_form.html',{'form':form})
    
def tweet_edit(request, tweet_id):
    instance = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('list')
    else:
        form = TweetForm(instance=instance)
        return render(request, 'tweet_form.html',{'form':form})

def tweet_delete(request,tweet_id):
    instance = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        instance.delete()
        return redirect('list')
    else:
        return render(request, 'tweet_delete.html')