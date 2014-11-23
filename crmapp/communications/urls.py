from django.conf.urls import patterns, url

comm_urls = patterns('',

    url(r'^$',
        'crmapp.communications.views.comm_detail', name="comm_detail"
    ),

)
