from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import * 

def index(request):
    topics = Topic.objects.all()
    category = Category.objects.all()
    user_count = User.objects.all().count()
    topic_count = topics.count()

    context = {
        'topics': topics,
        'category': category,
        'topic_count': topic_count,
        'user_count': user_count,
        
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
    sub_module = Submodule.objects.get(id=pk)
    article = get_object_or_404(Article, submodule=sub_module)
    context = {
      'submodule': sub_module,
        'article': article
        }
    return render(request, 'include/article.html',context)

