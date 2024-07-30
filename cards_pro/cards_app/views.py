from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect

# this functionallty use for authintation--------
from django.contrib.auth.decorators import login_required
from .forms import TweetForm,UserRegistrationForm
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'index.html')

# this functionalty , we want all tweet are conver into list/ we want all tweet list on one page
def tweet_list(request): # fun name it ur choice here
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,"tweet_list.html",{'tweets':tweets})

# use for create tweet---
@login_required
def tweet_create(request): #fun name its ur chice here
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES)      # user always exist inside request-
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')          #import redirect , we are redirect this fun to another fun
        
    else:                                      # if user send empety tweet so it will handle-
        form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})
    
# This functionality for edit the tweet-----
@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=="POST":
        form=TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')             #import redirect , we are redirect this fun to another fun, that's why not used .html
    else:
        form=TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})
    
# this functionality for delete the tweet---------
@login_required
def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=="POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})

def register(request):                  #note--all  form Related, .html file are create outside template
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])     #cleaned use for clean milious data , so on
            user.save()
            login(request,user)                                   #use for , if user are saved so automatically it will login--
            return redirect('tweet_list')

    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})    #create url----
  
    
    
    
    
    
# This is the CRUD based and authintation based project---------  
    
    
    
    
    
    
    
    
    
    
    
    
    