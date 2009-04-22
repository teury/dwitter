from django.http import HttpResponse 
from django.template import RequestContext, loader


def dashboard(request):
    ctx = {}

    ctx = RequestContext(request,ctx)
    t = loader.get_template('base.html')

    return HttpResponse(t.render(ctx))
