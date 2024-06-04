from django.shortcuts import render, get_object_or_404
from events.models import Event
from django.http import Http404


def index(request):
    context = {
        "test_context": "My Django Template with inheritance!",
        "events": Event.objects.all()
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def event_details(request, event_id):
    try:
        context = {
            "event": get_object_or_404(Event, id=event_id)
        }
        return render(request, "details.html", context)
    except Http404:
        return render(request, "404.html")
