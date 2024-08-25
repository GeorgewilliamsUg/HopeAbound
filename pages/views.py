from django.shortcuts import render, get_object_or_404
from .models import ChildProfile


def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')


def causes_view(request):
    return render(request, 'causes.html')


def cause_single_view(request):
    return render(request, 'cause_single.html')


def faqs_view(request):
    return render(request, 'faqs.html')


def events_view(request):
    return render(request, 'events.html')


def blog_view(request):
    return render(request, 'blog.html')


def event_single_view(request):
    return render(request, 'event_single.html')


def blog_single_view(request):
    return render(request, 'blog_single.html')


def gallery_view(request):
    return render(request, 'gallery.html')


def volunteers_view(request):
    return render(request, 'volunteers.html')


def sponsorship_view(request):
    children = ChildProfile.objects.all()
    return render(request, 'sponsorship.html', {'children': children})


def child_detail_view(request, pk):
    child = get_object_or_404(ChildProfile, pk=pk)
    return render(request, 'child_detail.html', {'child': child})


def child_detail(request, pk):
    child = get_object_or_404(ChildProfile, pk=pk)
    return render(request, 'child_detail.html', {'child': child})