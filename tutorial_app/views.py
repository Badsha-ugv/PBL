from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import * 

def index(request):
    topics = Topic.objects.all()

    context = {
        'topics': topics
        }

    return render(request, 'tutorial_app/index.html',context) 

def learn(request,id=None):
    topic = Topic.objects.get(id=id)
    module = Module.objects.filter(topic=topic) 
    context = {
        'topic': topic,
        'modules': module
        }
    return render(request, 'tutorial_app/learn.html',context) 



#hx request
def get_article(request,pk=None):
    print(' i am calling')
    module = Module.objects.get(id=pk)
    article = get_object_or_404(Article, module=module)
    context = {
      'module': module,
        'article': article
        }
    return render(request, 'include/article.html',context)

