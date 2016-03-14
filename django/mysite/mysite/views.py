import datetime
from django.shortcuts import render_to_response

from django.http import HttpResponse, Http404
from django.template.loader import get_template


def hello(request):
    return HttpResponse("Hello world")

def my_homepage_view(request):
    return HttpResponse("/")

def current_datetime(request):
    current_date  = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    #
    # return HttpResponse(html)
    return render_to_response('current_datetime.html', locals())

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    #assert False
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    hour_offset = offset
    next_time = dt
   # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    #return HttpResponse(html)
    return render_to_response('hours_ahead.html', locals())