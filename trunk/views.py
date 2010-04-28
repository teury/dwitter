from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader

from dweet.models import Dweety
from dweet.forms import DweetForm

def dashboard(request):
    ctx = {}
    ctx['dweetList'] = Dweety.objects.all() #[:20]
    ctx['dweetForm'] = DweetForm()

    ctx = RequestContext(request,ctx)
    t = loader.get_template('dashboard.html')

    return HttpResponse(t.render(ctx))

def dweetForm(request):
    if request.method == 'POST':
         form = DweetForm(request.POST)
         if form.is_valid():
             dweety = form.save(commit=False) #dont save the dweet, yet. We need to add user :)
             dweety.user = request.user
             dweety.save()

    return HttpResponseRedirect('/')


def deleteDweet(request, dweet_id):
    dweet = Dweety.objects.get(id=dweet_id)
    if dweet.user == request.user:
        dweet.delete()

    return HttpResponseRedirect('/')

