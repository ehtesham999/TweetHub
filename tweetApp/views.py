from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet
from django.contrib.auth import login 
from django.contrib.auth.forms import AuthenticationForm
from .forms import TweetForm, RegistrationForm
# Create your views here.
def home(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweet_list.html',{'tweets':tweets})

@login_required
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
    
@login_required
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

@login_required
def tweet_delete(request,tweet_id):
    instance = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        instance.delete()
        return redirect('list')
    else:
        return render(request, 'tweet_delete.html')
    

def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html',{'form':form})

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})