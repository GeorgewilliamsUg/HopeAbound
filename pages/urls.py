from django.urls import path
from .views import (
    home_view, about_view, contact_view, causes_view, cause_single_view, donate_view,
    faqs_view, events_view, blog_view, event_single_view, blog_single_view, gallery_view,
    volunteers_view, child_profile_view
)


urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('causes/', causes_view, name='causes'),
    path('causes/<int:cause_id>/', cause_single_view, name='cause_single'),
    path('donate/', donate_view, name='donate'),
    path('faqs/', faqs_view, name='faqs'),
    path('events/', events_view, name='events'),
    path('events/<int:event_id>/', event_single_view, name='event_single'),
    path('blog/', blog_view, name='blog'),
    path('blog/<int:blog_id>/', blog_single_view, name='blog_single'),
    path('gallery/', gallery_view, name='gallery'),
    path('volunteers/', volunteers_view, name='volunteers'),
    path('child-profiles/', child_profile_view, name='child_profiles'),
]
