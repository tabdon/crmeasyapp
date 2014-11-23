from django.conf.urls import patterns, include, url

from marketing.views import HomePage

urlpatterns = patterns('',

    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs
    url(r'^signup/$',
        'crmapp.subscribers.views.subscriber_new', name='sub_new'
    ),

    # Admin URL


    # Login/Logout URLs


    # Account related URLs


    # Contact related URLS


    # Communication related URLs

)