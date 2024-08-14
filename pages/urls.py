from django.urls import path
from .views import (home_view, about_view, volunteers_view, blog_view, gallery_view, blog_single_view,
                    donate_view, contact_view, causes_view, cause_single_view, events_view, event_single_view,
                    child_profile_view)


urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('blog/', blog_view, name='blog'),
    path('faq/', about_view, name='faq'),
    path('volunteers/', volunteers_view, name='volunteers'),
    path('blog/', blog_single_view, name='blog_single'),
    path('sponsorship/', child_profile_view, name='sponsorships'),
    path('gallery/', gallery_view, name='gallery'),
    path('blog/', blog_single_view, name='blog_single'),
    path('donate/', donate_view, name='donate'),
    path('causes/', causes_view, name='causes'),
    path('cause_single/', cause_single_view, name='cause_single'),
    path('events/', events_view, name='events'),
    path('event/', event_single_view, name='event_single'),
   ]
