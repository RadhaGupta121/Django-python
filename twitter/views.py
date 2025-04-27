from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from .models import Twitter
from .forms import TwitterForm,userRegistration
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login



# Create your views here.
def home(request):
    return render(request,'index.html')

def profile(request):
    user=request.user
    tweets=Twitter.objects.filter(user=user)
    return render(request,'profile.html',{
        'user':request.user,
        'tweets':tweets,

    })
@login_required
def newTweet(request):
    if request.method == 'POST':
        form=TwitterForm(request.POST, request.FILES)
        # print("this is inside the createtweeet view",form)
        if form.is_valid():
            tweet=form.save(commit=False)
            
            tweet.user=request.user
            tweet.save()
            return redirect('alltweets')
        # else:
        #     print('this is in else part')
        #     form= TwitterForm()
    else:
        form=TwitterForm()
    return render(request,'newTweet.html',{'form':form})


@login_required
def editTweet(request,tweet_id):
    tweet=get_object_or_404(Twitter,pk=tweet_id,user=request.user)
    if request.method == 'POST':
        form=TwitterForm(request.POST, request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('alltweets')

        
    else:
        form=TwitterForm(instance=tweet)
    return render(request,'newTweet.html',{'form':form})
   

        


def allTweets(request):
    tweets=Twitter.objects.all()
    print(tweets)
    return render(request,'alltweets.html',{'tweets':tweets})
    
@login_required 
def deleteTweet(request, tweet_id):
    tweet = get_object_or_404(Twitter, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('alltweets')
    return render(request, 'delete_confirm.html', {'tweets': tweet})

def registerUser(request):
    # email= forms.EmailField()
    if request.method=='POST':
        form=userRegistration(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('alltweets')
    else:
        form=userRegistration()
    return render(request,'registration/register.html',{'form':form})

@login_required

def searchbyUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        tweets=Twitter.objects.filter(user__username__icontains=username)
        return render(request,'alltweets.html',{'tweets':tweets})
    else:
        tweets=Twitter.objects.all()
    return render(request,'alltweets.html',{'tweets':tweets})

