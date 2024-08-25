from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    home_view, about_view, contact_view, causes_view, cause_single_view,
    faqs_view, events_view, blog_view, event_single_view, blog_single_view, gallery_view,
    volunteers_view, sponsorship_view, child_detail_view, child_detail
)

urlpatterns = [
                  path('', home_view, name='home'),
                  path('about/', about_view, name='about'),
                  path('contact/', contact_view, name='contact'),
                  path('causes/', causes_view, name='causes'),
                  path('causes/single/', cause_single_view, name='cause_single'),
                  path('faqs/', faqs_view, name='faqs'),
                  path('events/', events_view, name='events'),
                  path('event-single/', event_single_view, name='event_single'),
                  path('blog/', blog_view, name='blog'),
                  path('blog/single/', blog_single_view, name='blog_single'),
                  path('gallery/', gallery_view, name='gallery'),
                  path('volunteers/', volunteers_view, name='volunteers'),
                  path('sponsorship/', sponsorship_view, name='sponsorship'),
                  path('child/<int:child_id>/', child_detail_view, name='child_detail'),
                  path('child/<int:pk>/', child_detail, name='child_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
