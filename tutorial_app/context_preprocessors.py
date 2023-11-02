from .models import Topic

def get_topics(request):
    topics = Topic.objects.all()
    
    return {'topics': topics}