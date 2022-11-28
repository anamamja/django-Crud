from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import polls



def index(request):
    mypolls = polls.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mypolls': mypolls
    }
    return HttpResponse(template.render(context, request))
#
#
def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))




def addrecord(request):
    first = request.POST['first']
    last = request.POST['last']
    poll = polls(firstname=first, lastname=last)
    poll.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    poll = polls.objects.get(id=id)
    poll.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    mypoll = polls.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mypoll': mypoll,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  poll = polls.objects.get(id=id)
  poll.firstname = first
  poll.lastname = last
  poll.save()
  return HttpResponseRedirect(reverse('index'))



def read_file(request):
    with open('/Users/te-bd-abdulbasit/Desktop/djangoproject/polls/work.txt') as work:
        data = work.read()
        return HttpResponse(data,content_type='text/plain')



