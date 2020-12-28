from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
    'title':'My first blog',
    'author':'Nkaka Eric',
    'posted_date':'December,26,2020',
    'content':'Hello everyone how are you!'
    },
    {
    'title':'Greetings',
    'author':'Jane Doe',
    'posted_date':'november,2,2020',
    'content':'I am jane doe what about you!'
    },
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
